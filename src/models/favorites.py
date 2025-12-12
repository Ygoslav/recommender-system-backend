from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class FavoriteModel(Base):
    __tablename__ = 'favorites'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(nullable=False, unique=False)
    product_id: Mapped[int] = mapped_column(nullable=False, unique=False)
