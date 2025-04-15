# Fichier : tests/test_performance.py
import time
import pytest
from src.data_loader import load_ratings
from src.recommender import Recommender

def test_recommendation_performance():
    """Teste si les recommandations s'exécutent en moins de 1 seconde pour 100 utilisateurs."""
    ratings = load_ratings('data/user_ratings.csv')
    recommender = Recommender(ratings)
    
    start_time = time.time()
    recommender.recommend(0)
    end_time = time.time()
    
    assert end_time - start_time < 1.0, "Temps d'exécution trop long"