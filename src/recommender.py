# Fichier : src/recommender.py
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:
    def __init__(self, ratings: pd.DataFrame):
        self.ratings = ratings.fillna(0)  # Remplacer NaN par 0 pour le calcul de similarité
        self.user_similarity = cosine_similarity(self.ratings)
    
    def recommend(self, user_id: int, n_recommendations: int = 5) -> list:
        """Recommande des produits non notés par l'utilisateur."""
        # Trouver les produits non notés par l'utilisateur
        user_ratings = self.ratings.loc[user_id]
        unrated_products = user_ratings[user_ratings == 0].index.tolist()

        # Si tout est noté, retourne une liste vide
        if not unrated_products:
            return []

        # Calculer les scores prédits pour les produits non notés
        user_sim_scores = self.user_similarity[user_id]
        similar_users = np.argsort(-user_sim_scores)[1:]  # Exclure l'utilisateur lui-même

        # Agréger les notes des utilisateurs similaires pour les produits non notés
        recommendations = {}
        for product in unrated_products:
            product_ratings = self.ratings[product].iloc[similar_users]
            valid_ratings = product_ratings[product_ratings > 0]  # Ignorer les 0
            if not valid_ratings.empty:
                recommendations[product] = valid_ratings.mean()

        # Trier et retourner les top-N recommandations
        sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
        return [product for product, score in sorted_recommendations[:n_recommendations]]