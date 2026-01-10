from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from src import crud
from src.dependencies.auth import AuthenticationDependency
from src.dependencies.db import DatabaseDependency

router = APIRouter(prefix='/buy')


@router.post('')
async def buy_products(
    db: DatabaseDependency,
    user: AuthenticationDependency,
) -> JSONResponse:
    if crud.get_cart_items_count(db, user.id) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Cart is empty',
        )
    crud.close_cart(db, user.id)
    return {'ok': 'Success'}
