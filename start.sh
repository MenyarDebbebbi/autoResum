#!/bin/bash

# Script de démarrage pour AutoResum
# Lance le backend et le frontend en parallèle

echo "🚀 Démarrage d'AutoResum..."
echo "================================"

# Vérifier si Python est installé
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 n'est pas installé. Veuillez l'installer d'abord."
    exit 1
fi

# Vérifier si Node.js est installé
if ! command -v node &> /dev/null; then
    echo "❌ Node.js n'est pas installé. Veuillez l'installer d'abord."
    exit 1
fi

# Vérifier si npm est installé
if ! command -v npm &> /dev/null; then
    echo "❌ npm n'est pas installé. Veuillez l'installer d'abord."
    exit 1
fi

echo "✅ Vérifications des prérequis terminées"

# Fonction pour arrêter tous les processus
cleanup() {
    echo ""
    echo "🛑 Arrêt des services..."
    kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
    exit 0
}

# Capturer Ctrl+C pour arrêter proprement
trap cleanup SIGINT

# Démarrer le backend
echo "🔧 Démarrage du backend..."
cd backend

# Vérifier si les dépendances Python sont installées
if [ ! -d "venv" ]; then
    echo "📦 Création de l'environnement virtuel Python..."
    python3 -m venv venv
fi

# Activer l'environnement virtuel
source venv/bin/activate

# Installer les dépendances si nécessaire
if [ ! -f "venv/lib/python*/site-packages/fastapi" ]; then
    echo "📦 Installation des dépendances Python..."
    pip install -r requirements.txt
fi

# Démarrer le backend en arrière-plan
echo "🚀 Lancement du serveur backend sur http://localhost:8000"
python run.py &
BACKEND_PID=$!

# Attendre que le backend démarre
sleep 5

# Démarrer le frontend
echo "🎨 Démarrage du frontend..."
cd ../frontend

# Installer les dépendances Node.js si nécessaire
if [ ! -d "node_modules" ]; then
    echo "📦 Installation des dépendances Node.js..."
    npm install
fi

# Démarrer le frontend en arrière-plan
echo "🚀 Lancement du serveur frontend sur http://localhost:5173"
npm run dev &
FRONTEND_PID=$!

echo ""
echo "✅ AutoResum est maintenant en cours d'exécution !"
echo "================================"
echo "🌐 Frontend: http://localhost:5173"
echo "🔧 Backend:  http://localhost:8000"
echo "📚 API Docs: http://localhost:8000/docs"
echo ""
echo "Appuyez sur Ctrl+C pour arrêter tous les services"
echo "================================"

# Attendre que les processus se terminent
wait 