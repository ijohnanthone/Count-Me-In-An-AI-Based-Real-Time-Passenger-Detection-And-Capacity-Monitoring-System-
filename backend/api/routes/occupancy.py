"""
Occupancy data endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from schemas.occupancy import (
    OccupancyReadingCreate,
    OccupancyReadingResponse,
    OccupancyHistoryResponse,
    OccupancyCurrentResponse,
)
from database.db import get_db

router = APIRouter()


@router.post("/readings", response_model=OccupancyReadingResponse, status_code=status.HTTP_201_CREATED)
async def submit_occupancy_reading(
    reading_data: OccupancyReadingCreate,
    db: Session = Depends(get_db),
):
    """
    Submit occupancy reading from edge device.
    TODO: Implement occupancy reading submission.
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Occupancy submission not yet implemented",
    )


@router.get("/vehicles/{vehicle_id}/current", response_model=OccupancyCurrentResponse)
async def get_current_occupancy(
    vehicle_id: str,
    db: Session = Depends(get_db),
):
    """
    Get current occupancy for a vehicle.
    TODO: Implement get current occupancy logic.
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Get current occupancy not yet implemented",
    )


@router.get("/vehicles/{vehicle_id}/history", response_model=OccupancyHistoryResponse)
async def get_occupancy_history(
    vehicle_id: str,
    start_time: datetime = Query(None),
    end_time: datetime = Query(None),
    interval: str = Query("5m"),
    limit: int = Query(100, le=1000),
    db: Session = Depends(get_db),
):
    """
    Get occupancy history for a vehicle.
    TODO: Implement occupancy history retrieval.
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Occupancy history not yet implemented",
    )
