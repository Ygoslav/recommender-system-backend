from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class FavoriteModel(Base):
    __tablename__ = 'favorites'
    user_id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(primary_key=True)
