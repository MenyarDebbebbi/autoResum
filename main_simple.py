import sys
import os

# Ajouter le répertoire backend_simple au path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend_simple'))

from backend_simple.main import app

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port) 