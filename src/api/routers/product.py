from __future__ import annotations

from fastapi import APIRouter, HTTPException, status

from src.crud import get_product_by_id, get_products
from src.dependencies.db import DatabaseDependency
from src.schemas.products import ProductSchema

router = APIRouter()


@router.get('/product')
async def get_all_products(db: DatabaseDependency, skip: int = 0, limit: int = 100) -> list[ProductSchema]:
    return get_products(db, skip, limit)


@router.get('/product/{product_id}')
async def get_product(db: DatabaseDependency, product_id: int) -> ProductSchema:
    product = get_product_by_id(db, product_id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Product with id={product_id} does not exists',
        )
    return product
