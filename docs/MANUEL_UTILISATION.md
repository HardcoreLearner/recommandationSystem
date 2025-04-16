# Manuel d'utilisation

# 📚 Système de Recommandation Collaboratif

Un système de recommandation basé sur le filtrage collaboratif, développé avec Python et scikit-learn.

## 🚀 Fonctionnalités

- Génération de données utilisateurs/produits réalistes
- Algorithme de similarité cosinus entre utilisateurs
- Tests automatisés avec couverture complète
- Interface en ligne de commande simple

## 📦 Installation

### Prérequis
- Python 3.10+
- pip

# Cloner le dépôt
git clone https://github.com/votre-utilisateur/recommendation-system.git
cd recommendation-system

# Configurer l'environnement
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Installer les dépendances
pip install -r requirements.txt

## 🧠 Utilisation

### Générer des données

python3 generate_data.py

### Utilisation basique

from src.data_loader import load_ratings
from src.recommender import Recommender

#### Charger les données
ratings = load_ratings('data/user_ratings.csv')

#### Créer le moteur de recommandation
recommender = Recommender(ratings)

#### Obtenir des recommandations
print(recommender.recommend(user_id=0, n_recommendations=5))

### Interface CLI

python3 -m src.recommender --user_id 0 --n_reco 5

## 🗂 Structure du Projet

.
├── data/               # Données générées (CSV)
├── src/                # Code source
│   ├── data_loader.py  # Chargement des données
│   └── recommender.py  # Cœur du système
├── tests/              # Tests automatisés
├── docs/               # Documentation et visuels
├── requirements.txt    # Dépendances Python
└── generate_data.py    # Génération de données fictives

## 🧪 Tests

#### Lancer tous les tests
pytest tests/ -v

#### Générer le rapport de couverture
pytest --cov=src --cov-report=html

## 🙏 Remerciements

Bibliothèques : scikit-learn, pandas

Outils : pytest, Faker