import pytest
from src.data_loader import load_ratings

def test_load_ratings_basic():
    """Teste le chargement des données."""
    df = load_ratings('data/user_ratings.csv')
    assert df.shape == (100, 20), "La forme des données doit être (100, 20)"
    assert df.isna().sum().sum() > 0, "Il doit y avoir des valeurs manquantes (NaN)"

def test_load_ratings_invalid_path():
    """Teste la gestion d'une erreur de chemin invalide."""
    with pytest.raises(FileNotFoundError):
        load_ratings('chemin/inexistant.csv')