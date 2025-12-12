from __future__ import annotations

from fastapi import APIRouter, HTTPException, status

from src import crud
from src.dependencies.auth import AuthenticationDependency
from src.dependencies.db import DatabaseDependency
from src.schemas.products import ProductSchema

router = APIRouter()


@router.get('/favorite')
async def get_all_favorites_for_user(
    db: DatabaseDependency,
    user: AuthenticationDependency,
    skip: int = 0,
    limit: int | None = None,
    name: str | None = None,
) -> list[ProductSchema]:
    return crud.get_favorites_for_user(
        db,
        user.id,
        skip,
        limit,
        name,
    )


@router.post('/favorite', status_code=status.HTTP_201_CREATED)
async def add_to_favorites(
    db: DatabaseDependency,
    user: AuthenticationDependency,
    product_id: int,
) -> dict:
    if crud.get_favorite_for_user_by_product_id(
        db,
        user.id,
        product_id,
    ):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f'Product with id={product_id} already in favorites',
        )
    if not crud.get_product_by_id(db, product_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Product with id={product_id} does not exists',
        )
    crud.add_product_to_favorites(db, user.id, product_id)

    return {'ok': f'Product with id={product_id} successfully added to favorites'}


@router.delete('/favorite/{product_id}')
async def delete_from_favorites(
    db: DatabaseDependency,
    user: AuthenticationDependency,
    product_id: int,
) -> dict:
    if not crud.delete_product_from_favorites(
        db,
        user.id,
        product_id,
    ):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Product with id={product_id} not in favorites',
        )
    return {'ok': f'Product with id={product_id} successfully deleted from favorites'}
