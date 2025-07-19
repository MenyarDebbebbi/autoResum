from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import re
from typing import List

app = FastAPI(title="AutoResum API", version="1.0.0")

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "https://autoresum.netlify.app",
        "https://*.netlify.app",
        "https://*.railway.app",
        "https://*.render.com",
        "https://*.herokuapp.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextRequest(BaseModel):
    text: str
    max_length: int = 150

class SummaryResponse(BaseModel):
    summary: str
    original_length: int
    summary_length: int
    reduction_percentage: float

def simple_summarize(text: str, max_length: int = 150) -> str:
    """
    Résumé simple basé sur l'extraction de phrases clés
    """
    # Nettoyer le texte
    text = re.sub(r'\s+', ' ', text.strip())
    
    # Diviser en phrases
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    if not sentences:
        return "Texte trop court pour résumer."
    
    # Si le texte est déjà court, le retourner tel quel
    if len(text) <= max_length:
        return text
    
    # Sélectionner les premières phrases jusqu'à la limite
    summary = ""
    for sentence in sentences:
        if len(summary + sentence) <= max_length:
            summary += sentence + ". "
        else:
            break
    
    return summary.strip()

@app.get("/")
async def root():
    return {
        "message": "AutoResum API - Service de résumé automatique",
        "version": "1.0.0",
        "status": "online"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "autoresum-api"}

@app.post("/summarize", response_model=SummaryResponse)
async def summarize_text(request: TextRequest):
    try:
        if not request.text.strip():
            raise HTTPException(status_code=400, detail="Le texte ne peut pas être vide")
        
        original_length = len(request.text)
        summary = simple_summarize(request.text, request.max_length)
        summary_length = len(summary)
        
        reduction_percentage = ((original_length - summary_length) / original_length) * 100
        
        return SummaryResponse(
            summary=summary,
            original_length=original_length,
            summary_length=summary_length,
            reduction_percentage=round(reduction_percentage, 2)
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors du résumé: {str(e)}")

@app.get("/info")
async def get_info():
    return {
        "service": "AutoResum API",
        "description": "Service de résumé automatique de texte",
        "version": "1.0.0",
        "features": [
            "Résumé de texte simple",
            "Extraction de phrases clés",
            "API RESTful",
            "Support CORS"
        ],
        "endpoints": {
            "GET /": "Informations générales",
            "GET /health": "Vérification de santé",
            "POST /summarize": "Résumer un texte",
            "GET /info": "Informations détaillées"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 