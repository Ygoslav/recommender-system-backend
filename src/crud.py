from __future__ import annotations

from sqlalchemy.orm import Session

from src.models.favorites import FavoriteModel
from src.models.products import ProductModel
from src.models.users import UserModel
from src.schemas.users import UserCreateSchema


def get_user_by_id(db: Session, user_id: int) -> UserModel | None:
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_username(db: Session, username: str) -> UserModel | None:
    return db.query(UserModel).filter(UserModel.username == username).first()


def get_users(
    db: Session,
    skip: int = 0,
    limit: int | None = 100,
) -> list[UserModel]:
    return db.query(UserModel).offset(skip).limit(limit).all()


def add_user(db: Session, user: UserCreateSchema) -> UserModel:
    db_user = UserModel(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_product_by_id(db: Session, product_id: int) -> ProductModel | None:
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()


def get_product_by_name(db: Session, product_name: int) -> ProductModel | None:
    return db.query(ProductModel).filter(ProductModel.name == product_name).first()


def get_products(
    db: Session,
    skip: int = 0,
    limit: int | None = 100,
) -> list[ProductModel]:
    return db.query(ProductModel).offset(skip).limit(limit).all()


def get_favorites_for_user(
    db: Session,
    user_id: int,
    skip: int = 0,
    limit: int | None = 100,
) -> list[ProductModel]:
    return (
        db.query(ProductModel)
        .join(FavoriteModel, FavoriteModel.product_id == ProductModel.id)
        .filter(FavoriteModel.user_id == user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_favorite_for_user_by_product_id(
    db: Session,
    user_id: int,
    product_id: int,
) -> ProductModel | None:
    return (
        db.query(ProductModel)
        .join(FavoriteModel, FavoriteModel.product_id == ProductModel.id)
        .filter(FavoriteModel.product_id == product_id, FavoriteModel.user_id == user_id)
        .first()
    )


def add_product_to_favorites(
    db: Session,
    user_id: int,
    product_id: int,
) -> bool:
    if not get_product_by_id(db, product_id):
        return False
    new_favorite = FavoriteModel(user_id=user_id, product_id=product_id)
    db.add(new_favorite)
    db.commit()
    db.refresh(new_favorite)
    return True


def delete_product_from_favorites(db: Session, user_id: int, product_id: int) -> bool:
    favorite_product = (
        db.query(FavoriteModel)
        .filter(FavoriteModel.product_id == product_id, FavoriteModel.user_id == user_id)
        .first()
    )
    if not favorite_product:
        return False
    db.delete(favorite_product)
    db.commit()
    return True
