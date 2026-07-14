"""
Health check endpoints.
"""
from fastapi import APIRouter
from datetime import datetime

router = APIRouter()


@router.get("/health")
async def health_check():
    """
    Basic health check endpoint.
    """
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "Count-Me-In Backend",
    }


@router.get("/health/ready")
async def readiness_check():
    """
    Readiness check endpoint.
    """
    return {
        "ready": True,
        "timestamp": datetime.utcnow().isoformat(),
    }
