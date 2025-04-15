# Fichier : src/data_loader.py
import pandas as pd

def load_ratings(file_path: str) -> pd.DataFrame:
    """Charge les données et remplace les 0 par NaN pour les calculs de similarité."""
    df = pd.read_csv(file_path, index_col='user_id')
    df.replace(0, pd.NA, inplace=True)  # Traite les 0 comme des valeurs manquantes
    return df