from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class ProductModel(Base):
    __tablename__ = 'products'
    # __table_args__ = {'extend_existing': True}
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)
