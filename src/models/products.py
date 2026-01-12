from decimal import Decimal

from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class ProductModel(Base):
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column(nullable=False)
    website: Mapped[str]
    country: Mapped[str]
    category: Mapped[str]
    subcategory: Mapped[str]
    title_href: Mapped[str]
    price: Mapped[Decimal]
    brand: Mapped[str]
    ingredients: Mapped[str]
    form: Mapped[str]
    type: Mapped[str]
    color: Mapped[str]
    size: Mapped[Decimal]
    rating: Mapped[Decimal]
    noofratings: Mapped[int]
    has_allergen: Mapped[bool]
    has_fragrance: Mapped[bool]
    has_parfum: Mapped[bool]
    has_limonene: Mapped[bool]
    has_linalool: Mapped[bool]
    has_citral: Mapped[bool]
    has_citronellol: Mapped[bool]
    has_eugenol: Mapped[bool]
    has_hexyl_cinnamal: Mapped[bool]
    has_benzyl_alcohol: Mapped[bool]
    has_benzyl_salicylate: Mapped[bool]
    has_coumarin: Mapped[bool]
    has_alpha_isomethyl_ionone: Mapped[bool]
    has_cinnamal: Mapped[bool]
    has_isoeugenol: Mapped[bool]
    has_farnesol: Mapped[bool]
    has_geraniol: Mapped[bool]
    has_hydroxycitronellal: Mapped[bool]
    has_butylphenyl_methylpropional: Mapped[bool]
    has_methylisothiazolinone: Mapped[bool]
    has_methylchloroisothiazolinone: Mapped[bool]
    has_dmdm_hydantoin: Mapped[bool]
    has_formaldehyde: Mapped[bool]
    has_propylene_glycol: Mapped[bool]
