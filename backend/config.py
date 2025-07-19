import os
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

class Config:
    """Configuration de l'application AutoResum"""
    
    # Configuration de l'API
    API_TITLE = "AutoResum API"
    API_VERSION = "1.0.0"
    API_DESCRIPTION = "API pour le résumé automatique de texte avec IA"
    
    # Configuration du serveur
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
    
    # Configuration CORS
    CORS_ORIGINS = [
        "http://localhost:5173",  # Vite dev server
        "http://localhost:3000",  # Alternative
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000"
    ]
    
    # Configuration des modèles
    DEFAULT_MAX_LENGTH = 150
    DEFAULT_MIN_LENGTH = 50
    DEFAULT_LANGUAGE = "fr"
    
    # Configuration NLP
    MAX_KEYWORDS = 10
    MAX_ENTITIES = 10
    
    # Configuration des modèles HuggingFace
    FRENCH_MODEL = "csebuetnlp/mT5_multilingual_XLSum"
    ENGLISH_MODEL = "facebook/bart-large-cnn"
    FALLBACK_MODEL = "sshleifer/distilbart-cnn-12-6"
    
    # Configuration spaCy
    SPACY_MODEL_FR = "fr_core_news_sm"
    SPACY_MODEL_EN = "en_core_web_sm"
    
    # Configuration des logs
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Configuration de sécurité
    MAX_TEXT_LENGTH = 10000  # Longueur maximale du texte d'entrée
    MIN_TEXT_LENGTH = 50     # Longueur minimale du texte d'entrée
    
    # Configuration des métriques
    WORDS_PER_MINUTE_READING = 200
    WORDS_PER_MINUTE_SPEAKING = 150 