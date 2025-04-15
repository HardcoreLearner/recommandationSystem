from faker import Faker
import pandas as pd
import numpy as np

# Configurer la génération aléatoire pour la reproductibilité
np.random.seed(42)
fake = Faker()

# Générer 100 utilisateurs fictifs
users = []
for user_id in range(100):
    users.append({
        'user_id': user_id,
        'user_name': fake.name(),
        'email': fake.email()
    })

# Générer 20 produits fictifs
products = []
for product_id in range(20):
    products.append({
        'product_id': product_id,
        'product_name': fake.word().capitalize() + " " + fake.word().capitalize(),  # Ex: "Smartphone Case"
        'category': fake.random_element(elements=('Electronics', 'Books', 'Fashion')),
        'price': np.random.randint(10, 200)
    })

# Générer des notations aléatoires (1-5) utilisateurs -> produits
ratings_data = np.random.randint(1, 6, size=(100, 20))  # 100 utilisateurs x 20 produits
ratings_df = pd.DataFrame(ratings_data, columns=[f'product_{pid}' for pid in range(20)])
ratings_df.index.name = 'user_id'

# Sauvegarder en CSV
ratings_df.to_csv('data/user_ratings.csv')