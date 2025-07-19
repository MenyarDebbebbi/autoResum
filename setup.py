from setuptools import setup, find_packages

setup(
    name="autoresum",
    version="1.0.0",
    description="Application de résumé automatique de texte avec IA",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.104.1",
        "uvicorn[standard]==0.24.0",
        "python-multipart==0.0.6",
        "transformers==4.35.2",
        "torch>=2.2.0",
        "spacy==3.7.2",
        "nltk==3.8.1",
        "pydantic==2.5.0",
        "python-dotenv==1.0.0",
        "requests==2.31.0",
        "numpy>=1.26.0",
        "scikit-learn>=1.3.0",
    ],
    python_requires=">=3.9",
) 