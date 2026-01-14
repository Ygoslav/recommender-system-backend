from fastapi import APIRouter, HTTPException, status

from src import crud
from src.dependencies.auth import AuthenticationDependency
from src.dependencies.db import DatabaseDependency
from src.recommenders.v1 import CosmeticsRecommender
from src.recommenders.v2 import recommend_for_user
from src.schemas.products import ProductSchema

router = APIRouter(prefix='/recommendations')


@router.get('')
async def get_recommendations(
    db: DatabaseDependency,
    user: AuthenticationDependency,
    top_n: int = 5,
) -> list[int]:
    """
    Получает рекомендации косметики для авторизованного пользователя.
    """
    recommender = CosmeticsRecommender(db)
    if not recommender.train():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='Не достаточно данных для генерации рекомендаций.',
        )

    recommended_ids = recommender.recommend(user.id, top_n=top_n)
    if not recommended_ids:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Рекомендации не найдены.',
        )
    return recommended_ids


@router.get('/v2')
async def get_recommendations_v2(
    db: DatabaseDependency,
    user: AuthenticationDependency,
    top_n: int = 5,
) -> list[ProductSchema]:
    product_ids = recommend_for_user(user.id, db, top_n=top_n)
    products = [crud.get_product_by_id(db, pid) for pid in product_ids]
    return [ProductSchema.model_validate(p, from_attributes=True) for p in products if p]
