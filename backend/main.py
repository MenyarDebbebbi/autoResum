from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uvicorn
from services.summarizer import TextSummarizer
from services.nlp_processor import NLPProcessor

app = FastAPI(
    title="AutoResum API",
    description="API pour le résumé automatique de texte avec IA",
    version="1.0.0"
)

# Configuration CORS pour permettre les requêtes depuis le frontend Vue
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Frontend Vue
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialisation des services
summarizer = TextSummarizer()
nlp_processor = NLPProcessor()

class TextRequest(BaseModel):
    text: str
    max_length: Optional[int] = 150
    min_length: Optional[int] = 50
    language: Optional[str] = "fr"

class SummaryResponse(BaseModel):
    summary: str
    original_length: int
    summary_length: int
    compression_ratio: float
    keywords: list[str]
    reading_time: float

@app.get("/")
async def root():
    return {"message": "AutoResum API - Service de résumé automatique"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "services": {"summarizer": "ready", "nlp": "ready"}}

@app.post("/summarize", response_model=SummaryResponse)
async def summarize_text(request: TextRequest):
    """
    Résume automatiquement le texte fourni en utilisant l'IA
    """
    try:
        if not request.text.strip():
            raise HTTPException(status_code=400, detail="Le texte ne peut pas être vide")
        
        if len(request.text) < 50:
            raise HTTPException(status_code=400, detail="Le texte doit contenir au moins 50 caractères")
        
        # Traitement NLP pour extraire les mots-clés
        keywords = nlp_processor.extract_keywords(request.text)
        
        # Génération du résumé
        summary = summarizer.summarize(
            text=request.text,
            max_length=request.max_length,
            min_length=request.min_length,
            language=request.language
        )
        
        # Calcul des métriques
        original_length = len(request.text)
        summary_length = len(summary)
        compression_ratio = round((1 - summary_length / original_length) * 100, 2)
        reading_time = round(summary_length / 200, 1)  # Estimation: 200 mots/minute
        
        return SummaryResponse(
            summary=summary,
            original_length=original_length,
            summary_length=summary_length,
            compression_ratio=compression_ratio,
            keywords=keywords,
            reading_time=reading_time
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors du résumé: {str(e)}")

@app.post("/analyze")
async def analyze_text(request: TextRequest):
    """
    Analyse le texte sans le résumer (mots-clés, sentiment, etc.)
    """
    try:
        if not request.text.strip():
            raise HTTPException(status_code=400, detail="Le texte ne peut pas être vide")
        
        # Analyse complète du texte
        analysis = nlp_processor.analyze_text(request.text)
        
        return {
            "keywords": analysis["keywords"],
            "sentiment": analysis["sentiment"],
            "entities": analysis["entities"],
            "word_count": analysis["word_count"],
            "sentence_count": analysis["sentence_count"],
            "reading_time": analysis["reading_time"]
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'analyse: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 