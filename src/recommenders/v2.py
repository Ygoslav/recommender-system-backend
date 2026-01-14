from __future__ import annotations

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sqlalchemy import func
from sqlalchemy.orm import Session

from src.models.favorites import FavoriteModel


def build_user_item_matrix(db: Session) -> tuple[None, None] | pd.DataFrame:
    # Получаем все записи из favorites
    favorites = db.query(FavoriteModel).all()
    if not favorites:
        return None, None

    user_ids = [f.user_id for f in favorites]
    product_ids = [f.product_id for f in favorites]

    df = pd.DataFrame({
        'user_id': user_ids,
        'product_id': product_ids,
    })

    # Создаём бинарную матрицу: 1 если пользователь добавил товар в избранное
    user_item_matrix = df.pivot_table(
        index='user_id',
        columns='product_id',
        values='user_id',
        aggfunc=lambda x: 1,
        fill_value=0,
    )
    return user_item_matrix

def get_similar_products(product_id: int, user_item_matrix: pd.DataFrame, top_n: int = 5) -> list:
    # Транспонируем, чтобы получить item-item схожесть
    item_item_sim = cosine_similarity(user_item_matrix.T)
    item_item_df = pd.DataFrame(
        item_item_sim,
        index=user_item_matrix.columns,
        columns=user_item_matrix.columns,
    )

    if product_id not in item_item_df.index:
        return []

    # Находим наиболее похожие товары (исключая сам товар)
    similar = item_item_df[product_id].sort_values(ascending=False)[1:top_n+1]
    return similar.index.tolist()

def recommend_for_user(user_id: int, db: Session, top_n: int = 5) -> list:
    user_item_matrix = build_user_item_matrix(db)
    if user_item_matrix is None or user_id not in user_item_matrix.index:
        # Если пользователь ничего не добавлял — вернём популярные товары
        return get_popular_products(db, top_n)

    # Получаем товары, которые пользователь уже лайкнул
    liked_products = user_item_matrix.loc[user_id]
    liked_products = liked_products[liked_products > 0].index.tolist()

    if not liked_products:
        return get_popular_products(db, top_n)

    # Собираем рекомендации на основе всех лайкнутых товаров
    recommendations = set()
    for pid in liked_products:
        similar = get_similar_products(pid, user_item_matrix, top_n)
        recommendations.update(similar)

    # Убираем уже лайкнутые
    recommendations = [pid for pid in recommendations if pid not in liked_products]
    return recommendations[:top_n]

def get_popular_products(db: Session, top_n: int = 5) -> list:
    popular = (
        db.query(FavoriteModel.product_id, func.count(FavoriteModel.product_id).label('cnt'))
        .group_by(FavoriteModel.product_id)
        .order_by(func.count(FavoriteModel.product_id).desc())
        .limit(top_n)
        .all()
    )
    return [pid for pid, _ in popular]
