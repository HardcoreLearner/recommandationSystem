# Fichier : test.py
import sys
import pandas as pd
from src.data_loader import load_ratings
from src.recommender import Recommender

# Charger les données
ratings = load_ratings('data/user_ratings.csv')

# Vérifier que les données sont correctement chargées
print("Aperçu des données chargées :")
print(ratings.head())

# Initialiser le moteur
recommender = Recommender(ratings)

# Test avec l'utilisateur 0
print("\nRecommandations pour l'utilisateur 0 :", recommender.recommend(0, n_recommendations=3))