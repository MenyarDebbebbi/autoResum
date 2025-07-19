#!/usr/bin/env python3
"""
Point d'entrée principal pour Railway
Ce fichier importe et lance l'application FastAPI du backend
"""

import sys
import os

# Ajouter le dossier backend au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

# Importer et lancer l'application
from backend.main import app
import uvicorn

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port) 