from enum import StrEnum

from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class CartStatus(StrEnum):
    ACTIVE = 'active'
    CLOSED = 'closed'


class CartModel(Base):
    __tablename__ = 'carts'
    id: Mapped[int] = mapped_column(primary_key=True)
    current_status: Mapped[str] = mapped_column(
        nullable=False,
        default=CartStatus.ACTIVE,
    )
    user_id: Mapped[int] = mapped_column(nullable=False)


class CartItemsModel(Base):
    __tablename__ = 'cart_items'
    cart_id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[int] = mapped_column(nullable=False)
