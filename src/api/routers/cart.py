from typing import Annotated

from fastapi import APIRouter, HTTPException, status
from fastapi.params import Query
from fastapi.responses import JSONResponse

from src import crud
from src.dependencies.auth import AuthenticationDependency
from src.dependencies.db import DatabaseDependency
from src.schemas.cart import CartItemSchema

router = APIRouter(prefix='/cart')


@router.get('')
async def get_products_from_cart(
    db: DatabaseDependency,
    user: AuthenticationDependency,
) -> list[CartItemSchema]:
    return crud.get_cart(db, user.id)


@router.post('')
async def add_product_to_cart(
    db: DatabaseDependency,
    user: AuthenticationDependency,
    product_id: int,
    quantity: Annotated[int, Query(ge=1)] = 1,
) -> JSONResponse:
    if not crud.get_product_by_id(db, product_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Product with id={product_id} does not exists',
        )
    crud.add_product_to_cart(
        db,
        user.id,
        product_id,
        quantity,
    )
    return {'ok': f'{quantity} product with id={product_id} successfully added to cart'}


@router.delete('/{product_id}')
async def delete_product_from_cart(
    db: DatabaseDependency,
    user: AuthenticationDependency,
    product_id: int,
) -> JSONResponse:
    if not crud.delete_product_from_cart(db, user.id, product_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Product with id={product_id} not in cart',
        )
    return {'ok': f'Product with id={product_id} successfully deleted from cart'}
