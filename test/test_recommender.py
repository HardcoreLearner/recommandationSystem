import pytest
import pandas as pd
from src.data_loader import load_ratings
from src.recommender import Recommender

@pytest.fixture
def sample_ratings():
    """Simule un petit jeu de données pour les tests."""
    data = {
        'product_0': [5, 0, 3],
        'product_1': [0, 4, 0],
        'product_2': [2, 0, 0]
    }
    return pd.DataFrame(data)

def test_recommendations_for_user_with_unrated_products(sample_ratings):
    """Teste si des recommandations sont générées quand l'utilisateur a des produits non notés."""
    recommender = Recommender(sample_ratings)
    recommendations = recommender.recommend(0, n_recommendations=2)
    assert len(recommendations) > 0, "Doit recommander des produits non notés"

def test_no_recommendations_when_all_rated(sample_ratings):
    """Teste le cas où l'utilisateur a tout noté."""
    # Utilisateur 1 a tout noté (0 = non noté dans les données simulées)
    sample_ratings.loc[1] = [5, 4, 3]  # Tous les produits notés
    recommender = Recommender(sample_ratings)
    recommendations = recommender.recommend(1)
    assert len(recommendations) == 0, "Aucune recommandation attendue"


def test_recommendations_avoid_already_rated_products():
    """Vérifie que les produits déjà notés par l'utilisateur ne sont pas recommandés."""
    # Créer un scénario où l'utilisateur 0 a noté le product_0
    data = {
        'product_0': [5, 0, 0],  # Utilisateur 0 a noté product_0
        'product_1': [0, 4, 0],
        'product_2': [0, 0, 3]
    }
    ratings = pd.DataFrame(data)
    recommender = Recommender(ratings)
    recommendations = recommender.recommend(0)
    assert 'product_0' not in recommendations, "Le produit déjà noté ne doit pas être recommandé"

def test_recommendations_for_user_with_no_similar_users():
    """Teste un utilisateur sans similarité avec les autres (ex: notes radicalement différentes)."""
    # Créer un jeu de données où l'utilisateur 0 est unique
    data = {
        'product_0': [5, 1, 1],  # Utilisateur 0 très différent
        'product_1': [5, 1, 1],
        'product_2': [5, 1, 1]
    }
    ratings = pd.DataFrame(data)
    recommender = Recommender(ratings)
    recommendations = recommender.recommend(0)
    # Même sans similarité, le système peut recommander (à adapter selon l'algorithme)
    assert isinstance(recommendations, list), "Doit retourner une liste (même vide)"

def test_recommendation_product_format():
    """Vérifie que les IDs des produits recommandés sont au format attendu (ex: 'product_12')."""
    ratings = load_ratings('data/user_ratings.csv')
    recommender = Recommender(ratings)
    recommendations = recommender.recommend(0)
    for product in recommendations:
        assert product.startswith('product_'), f"ID de produit invalide : {product}"