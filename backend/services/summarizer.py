from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from typing import Optional
import logging

class TextSummarizer:
    """
    Service de résumé automatique utilisant les modèles transformers
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.models = {}
        self.tokenizers = {}
        self._load_models()
    
    def _load_models(self):
        """
        Charge les modèles de résumé pour différentes langues
        """
        try:
            # Modèle français - BART pour le français
            self.logger.info("Chargement du modèle français...")
            self.models["fr"] = pipeline(
                "summarization",
                model="csebuetnlp/mT5_multilingual_XLSum",
                tokenizer="csebuetnlp/mT5_multilingual_XLSum",
                device=0 if torch.cuda.is_available() else -1
            )
            
            # Modèle anglais - BART pour l'anglais
            self.logger.info("Chargement du modèle anglais...")
            self.models["en"] = pipeline(
                "summarization",
                model="facebook/bart-large-cnn",
                device=0 if torch.cuda.is_available() else -1
            )
            
            # Modèle multilingue de secours
            self.logger.info("Chargement du modèle multilingue...")
            self.models["multilingual"] = pipeline(
                "summarization",
                model="csebuetnlp/mT5_multilingual_XLSum",
                device=0 if torch.cuda.is_available() else -1
            )
            
            self.logger.info("Tous les modèles chargés avec succès")
            
        except Exception as e:
            self.logger.error(f"Erreur lors du chargement des modèles: {e}")
            # Fallback vers un modèle plus simple
            self._load_fallback_model()
    
    def _load_fallback_model(self):
        """
        Charge un modèle de secours plus simple
        """
        try:
            self.logger.info("Chargement du modèle de secours...")
            self.models["fallback"] = pipeline(
                "summarization",
                model="sshleifer/distilbart-cnn-12-6",
                device=0 if torch.cuda.is_available() else -1
            )
        except Exception as e:
            self.logger.error(f"Erreur lors du chargement du modèle de secours: {e}")
            raise Exception("Impossible de charger les modèles de résumé")
    
    def _detect_language(self, text: str) -> str:
        """
        Détection simple de la langue basée sur les caractères
        """
        # Détection basique basée sur les caractères français
        french_chars = set('àâäéèêëïîôöùûüÿç')
        text_chars = set(text.lower())
        
        if french_chars.intersection(text_chars):
            return "fr"
        else:
            return "en"
    
    def _truncate_text(self, text: str, max_tokens: int = 1024) -> str:
        """
        Tronque le texte pour respecter les limites du modèle
        """
        words = text.split()
        if len(words) > max_tokens:
            return " ".join(words[:max_tokens])
        return text
    
    def summarize(self, text: str, max_length: int = 150, min_length: int = 50, language: str = "fr") -> str:
        """
        Génère un résumé du texte fourni
        
        Args:
            text: Texte à résumer
            max_length: Longueur maximale du résumé
            min_length: Longueur minimale du résumé
            language: Langue du texte ("fr", "en", "auto")
        
        Returns:
            Résumé généré
        """
        try:
            # Détection automatique de la langue si demandée
            if language == "auto":
                language = self._detect_language(text)
            
            # Sélection du modèle approprié
            if language in self.models:
                model = self.models[language]
            elif "fr" in self.models:
                model = self.models["fr"]
            elif "multilingual" in self.models:
                model = self.models["multilingual"]
            else:
                model = self.models.get("fallback")
            
            if not model:
                raise Exception("Aucun modèle disponible pour le résumé")
            
            # Troncature du texte si nécessaire
            truncated_text = self._truncate_text(text)
            
            # Génération du résumé
            result = model(
                truncated_text,
                max_length=max_length,
                min_length=min_length,
                do_sample=False,
                num_beams=4,
                early_stopping=True
            )
            
            summary = result[0]['summary_text'].strip()
            
            # Nettoyage du résumé
            summary = self._clean_summary(summary)
            
            return summary
            
        except Exception as e:
            self.logger.error(f"Erreur lors du résumé: {e}")
            # Fallback vers une méthode simple
            return self._simple_summary(text, max_length)
    
    def _clean_summary(self, summary: str) -> str:
        """
        Nettoie et améliore le résumé généré
        """
        # Suppression des espaces multiples
        summary = " ".join(summary.split())
        
        # Capitalisation de la première lettre
        if summary and not summary[0].isupper():
            summary = summary[0].upper() + summary[1:]
        
        # Ajout d'un point final si nécessaire
        if summary and not summary.endswith(('.', '!', '?')):
            summary += '.'
        
        return summary
    
    def _simple_summary(self, text: str, max_length: int) -> str:
        """
        Méthode de résumé simple basée sur l'extraction de phrases
        """
        sentences = text.split('.')
        if len(sentences) <= 2:
            return text[:max_length] + "..." if len(text) > max_length else text
        
        # Prendre les premières phrases jusqu'à la limite
        summary_sentences = []
        current_length = 0
        
        for sentence in sentences:
            if current_length + len(sentence) <= max_length:
                summary_sentences.append(sentence.strip())
                current_length += len(sentence)
            else:
                break
        
        summary = ". ".join(summary_sentences)
        if summary and not summary.endswith('.'):
            summary += '.'
        
        return summary 