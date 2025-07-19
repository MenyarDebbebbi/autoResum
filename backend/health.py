from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check():
    """Endpoint de santé pour Railway"""
    return {
        "status": "healthy",
        "message": "AutoResum API is running",
        "version": "1.0.0"
    } 