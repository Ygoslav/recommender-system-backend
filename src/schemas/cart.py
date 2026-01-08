from pydantic import BaseModel

from src.schemas.products import ProductSchema


class CartItemSchema(BaseModel):
    product: ProductSchema
    quantity: int
