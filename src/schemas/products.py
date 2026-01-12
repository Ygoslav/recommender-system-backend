from __future__ import annotations

from decimal import Decimal

from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: int
    product_name: str
    website: str
    country: str
    category: str
    subcategory: str
    title_href: str
    price: Decimal | None
    brand: str
    ingredients: str
    form: str
    type: str
    color: str
    size: Decimal
    rating: Decimal
    noofratings: int
    has_allergen: bool
    has_fragrance: bool
    has_parfum: bool
    has_limonene: bool
    has_linalool: bool
    has_citral: bool
    has_citronellol: bool
    has_eugenol: bool
    has_hexyl_cinnamal: bool
    has_benzyl_alcohol: bool
    has_benzyl_salicylate: bool
    has_coumarin: bool
    has_alpha_isomethyl_ionone: bool
    has_cinnamal: bool
    has_isoeugenol: bool
    has_farnesol: bool
    has_geraniol: bool
    has_hydroxycitronellal: bool
    has_butylphenyl_methylpropional: bool
    has_methylisothiazolinone: bool
    has_methylchloroisothiazolinone: bool
    has_dmdm_hydantoin: bool
    has_formaldehyde: bool
    has_propylene_glycol: bool
