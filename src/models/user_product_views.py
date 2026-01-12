from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class UserProductViewsModel(Base):
    __tablename__ = 'user_product_views'
    user_id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(primary_key=True)
    views_count: Mapped[int] = mapped_column(nullable=False)
