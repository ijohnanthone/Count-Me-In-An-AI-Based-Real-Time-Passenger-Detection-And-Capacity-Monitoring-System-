"""
Authentication endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.user import UserLogin, UserCreate, TokenResponse, UserResponse
from database.db import get_db

router = APIRouter()


@router.post("/login", response_model=TokenResponse)
async def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    """
    User login endpoint.
    TODO: Implement authentication logic.
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Login endpoint not yet implemented",
    )


@router.post("/register", response_model=UserResponse)
async def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """
    User registration endpoint.
    TODO: Implement user registration logic.
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Registration endpoint not yet implemented",
    )


@router.post("/logout")
async def logout():
    """
    User logout endpoint.
    TODO: Implement logout logic.
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Logout endpoint not yet implemented",
    )


@router.post("/refresh")
async def refresh_token():
    """
    Refresh authentication token.
    TODO: Implement token refresh logic.
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Token refresh not yet implemented",
    )
