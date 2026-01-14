import numpy as np
from sklearn.decomposition import TruncatedSVD
from sqlalchemy.orm import Session

from src.models.favorites import FavoriteModel
from src.models.products import ProductModel
from src.models.users import UserModel


class CosmeticsRecommender:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.model = None
        self.user_id_to_index = {}
        self.product_id_to_index = {}
        self.index_to_product_id = {}
        self.rating_matrix = None

    def _load_data(self) -> bool:
        users = self.db.query(UserModel).all()
        products = self.db.query(ProductModel).all()

        if not users or not products:
            return False

        self.user_id_to_index = {u.id: i for i, u in enumerate(users)}
        self.product_id_to_index = {p.id: i for i, p in enumerate(products)}
        self.index_to_product_id = {i: p.id for i, p in enumerate(products)}

        R = np.zeros((len(users), len(products)))
        favorites = self.db.query(FavoriteModel).all()
        for fav in favorites:
            ui = self.user_id_to_index.get(fav.user_id)
            pi = self.product_id_to_index.get(fav.product_id)
            if ui is not None and pi is not None:
                R[ui, pi] = 1.0

        self.rating_matrix = R
        return True

    def train(self) -> bool:
        if not self._load_data():
            return False
        if self.rating_matrix.sum() == 0:
            return False
        self.model = TruncatedSVD(
            n_components=min(10, min(self.rating_matrix.shape) - 1),
            random_state=42,
        )
        self.model.fit(self.rating_matrix)
        return True

    def recommend(self, user_id: int, top_n: int = 5) -> list[int]:
        if self.model is None:
            return []
        if user_id not in self.user_id_to_index:
            return []

        user_idx = self.user_id_to_index[user_id]
        user_row = self.rating_matrix[user_idx : user_idx + 1]
        pred = self.model.inverse_transform(self.model.transform(user_row))[0]

        # Исключаем уже добавленные в избранное
        existing_favs = {
            fav.product_id
            for fav in self.db.query(FavoriteModel)
            .filter(FavoriteModel.user_id == user_id)
            .all()
        }

        recommendations = []
        for idx, score in enumerate(pred):
            prod_id = self.index_to_product_id[idx]
            if prod_id not in existing_favs:
                recommendations.append((score, prod_id))

        recommendations.sort(reverse=True)
        return [prod_id for _, prod_id in recommendations[:top_n]]
