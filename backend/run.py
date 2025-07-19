#!/usr/bin/env python3
"""
Script de démarrage pour AutoResum API
"""

import uvicorn
import logging
from config import Config

# Configuration des logs
logging.basicConfig(
    level=getattr(logging, Config.LOG_LEVEL),
    format=Config.LOG_FORMAT
)

logger = logging.getLogger(__name__)

def main():
    """Fonction principale pour démarrer le serveur"""
    try:
        logger.info("Démarrage de AutoResum API...")
        logger.info(f"Configuration: HOST={Config.HOST}, PORT={Config.PORT}, DEBUG={Config.DEBUG}")
        
        uvicorn.run(
            "main:app",
            host=Config.HOST,
            port=Config.PORT,
            reload=Config.DEBUG,
            log_level=Config.LOG_LEVEL.lower()
        )
        
    except KeyboardInterrupt:
        logger.info("Arrêt du serveur...")
    except Exception as e:
        logger.error(f"Erreur lors du démarrage: {e}")
        raise

if __name__ == "__main__":
    main() 