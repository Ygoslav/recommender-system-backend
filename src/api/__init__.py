from fastapi import APIRouter

from src.api.routers.cart import router as cart_router
from src.api.routers.favorite import router as favorites_router
from src.api.routers.product import router as product_router
from src.api.routers.register import router as register_router

main_router = APIRouter()

main_router.include_router(register_router)
main_router.include_router(product_router)
main_router.include_router(favorites_router)
main_router.include_router(cart_router)
