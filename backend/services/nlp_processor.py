import spacy
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter
import re
import logging
from typing import List, Dict, Any

class NLPProcessor:
    """
    Service de traitement NLP utilisant spaCy et NLTK
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.nlp = None
        self.stop_words = set()
        self.sentiment_analyzer = None
        self._initialize_nlp()
    
    def _initialize_nlp(self):
        """
        Initialise les modèles NLP
        """
        try:
            # Téléchargement des ressources NLTK nécessaires
            try:
                nltk.data.find('tokenizers/punkt')
            except LookupError:
                nltk.download('punkt')
            
            try:
                nltk.data.find('corpora/stopwords')
            except LookupError:
                nltk.download('stopwords')
            
            try:
                nltk.data.find('vader_lexicon')
            except LookupError:
                nltk.download('vader_lexicon')
            
            # Chargement du modèle spaCy
            try:
                self.nlp = spacy.load("fr_core_news_sm")
                self.logger.info("Modèle spaCy français chargé")
            except OSError:
                try:
                    self.nlp = spacy.load("en_core_web_sm")
                    self.logger.info("Modèle spaCy anglais chargé")
                except OSError:
                    self.logger.warning("Modèle spaCy non trouvé, utilisation de NLTK uniquement")
                    self.nlp = None
            
            # Initialisation des stop words
            self.stop_words = set(stopwords.words('french') + stopwords.words('english'))
            
            # Initialisation de l'analyseur de sentiment
            self.sentiment_analyzer = SentimentIntensityAnalyzer()
            
            self.logger.info("NLP Processor initialisé avec succès")
            
        except Exception as e:
            self.logger.error(f"Erreur lors de l'initialisation NLP: {e}")
            raise Exception("Impossible d'initialiser le processeur NLP")
    
    def extract_keywords(self, text: str, max_keywords: int = 10) -> List[str]:
        """
        Extrait les mots-clés du texte
        
        Args:
            text: Texte à analyser
            max_keywords: Nombre maximum de mots-clés à extraire
        
        Returns:
            Liste des mots-clés
        """
        try:
            # Nettoyage du texte
            cleaned_text = self._clean_text(text)
            
            # Tokenization
            if self.nlp:
                # Utilisation de spaCy si disponible
                doc = self.nlp(cleaned_text)
                keywords = []
                
                for token in doc:
                    if (token.is_alpha and 
                        not token.is_stop and 
                        not token.is_punct and
                        len(token.text) > 2 and
                        token.pos_ in ['NOUN', 'PROPN', 'ADJ', 'VERB']):
                        keywords.append(token.lemma_.lower())
                
                # Comptage des occurrences
                keyword_counts = Counter(keywords)
                
            else:
                # Fallback vers NLTK
                tokens = word_tokenize(cleaned_text.lower())
                keywords = [token for token in tokens 
                          if token.isalpha() and 
                          token not in self.stop_words and 
                          len(token) > 2]
                
                keyword_counts = Counter(keywords)
            
            # Sélection des mots-clés les plus fréquents
            top_keywords = [word for word, count in keyword_counts.most_common(max_keywords)]
            
            return top_keywords[:max_keywords]
            
        except Exception as e:
            self.logger.error(f"Erreur lors de l'extraction des mots-clés: {e}")
            return []
    
    def analyze_text(self, text: str) -> Dict[str, Any]:
        """
        Analyse complète du texte
        
        Args:
            text: Texte à analyser
        
        Returns:
            Dictionnaire contenant l'analyse complète
        """
        try:
            # Nettoyage du texte
            cleaned_text = self._clean_text(text)
            
            # Statistiques de base
            word_count = len(cleaned_text.split())
            sentence_count = len(sent_tokenize(cleaned_text))
            reading_time = round(word_count / 200, 1)  # 200 mots/minute
            
            # Extraction des mots-clés
            keywords = self.extract_keywords(text)
            
            # Analyse du sentiment
            sentiment = self._analyze_sentiment(cleaned_text)
            
            # Extraction des entités nommées
            entities = self._extract_entities(cleaned_text)
            
            return {
                "keywords": keywords,
                "sentiment": sentiment,
                "entities": entities,
                "word_count": word_count,
                "sentence_count": sentence_count,
                "reading_time": reading_time,
                "avg_sentence_length": round(word_count / sentence_count, 1) if sentence_count > 0 else 0
            }
            
        except Exception as e:
            self.logger.error(f"Erreur lors de l'analyse du texte: {e}")
            return {
                "keywords": [],
                "sentiment": {"compound": 0, "pos": 0, "neg": 0, "neu": 1},
                "entities": [],
                "word_count": 0,
                "sentence_count": 0,
                "reading_time": 0,
                "avg_sentence_length": 0
            }
    
    def _clean_text(self, text: str) -> str:
        """
        Nettoie le texte en supprimant les caractères spéciaux
        """
        # Suppression des caractères spéciaux mais conservation des accents
        cleaned = re.sub(r'[^\w\s\.\!\?\,\;\:\-\(\)]', '', text)
        # Suppression des espaces multiples
        cleaned = re.sub(r'\s+', ' ', cleaned)
        return cleaned.strip()
    
    def _analyze_sentiment(self, text: str) -> Dict[str, float]:
        """
        Analyse le sentiment du texte
        """
        try:
            if self.sentiment_analyzer:
                scores = self.sentiment_analyzer.polarity_scores(text)
                return {
                    "compound": round(scores['compound'], 3),
                    "positive": round(scores['pos'], 3),
                    "negative": round(scores['neg'], 3),
                    "neutral": round(scores['neu'], 3)
                }
            else:
                return {"compound": 0, "positive": 0, "negative": 0, "neutral": 1}
        except Exception as e:
            self.logger.error(f"Erreur lors de l'analyse de sentiment: {e}")
            return {"compound": 0, "positive": 0, "negative": 0, "neutral": 1}
    
    def _extract_entities(self, text: str) -> List[Dict[str, str]]:
        """
        Extrait les entités nommées du texte
        """
        try:
            if self.nlp:
                doc = self.nlp(text)
                entities = []
                
                for ent in doc.ents:
                    entities.append({
                        "text": ent.text,
                        "label": ent.label_,
                        "description": spacy.explain(ent.label_)
                    })
                
                return entities[:10]  # Limite à 10 entités
            else:
                return []
                
        except Exception as e:
            self.logger.error(f"Erreur lors de l'extraction des entités: {e}")
            return []
    
    def get_text_statistics(self, text: str) -> Dict[str, Any]:
        """
        Calcule les statistiques du texte
        """
        try:
            cleaned_text = self._clean_text(text)
            words = cleaned_text.split()
            sentences = sent_tokenize(cleaned_text)
            
            return {
                "total_characters": len(text),
                "total_words": len(words),
                "total_sentences": len(sentences),
                "avg_word_length": round(sum(len(word) for word in words) / len(words), 1) if words else 0,
                "avg_sentence_length": round(len(words) / len(sentences), 1) if sentences else 0,
                "reading_time_minutes": round(len(words) / 200, 1),
                "speaking_time_minutes": round(len(words) / 150, 1)
            }
            
        except Exception as e:
            self.logger.error(f"Erreur lors du calcul des statistiques: {e}")
            return {} 