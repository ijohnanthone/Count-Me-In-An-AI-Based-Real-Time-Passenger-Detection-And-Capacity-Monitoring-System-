"""
Occupancy Pydantic schemas for validation.
"""
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime


class OccupancyReadingCreate(BaseModel):
    """
    Schema for creating occupancy reading (from edge device).
    """
    vehicle_id: str
    person_count: int = Field(..., ge=0)
    occupancy_percentage: float = Field(..., ge=0, le=100)
    confidence: float = Field(default=0.0, ge=0, le=1)
    recorded_at: Optional[datetime] = None
    processing_time_ms: Optional[int] = None
    edge_device_id: Optional[str] = None
    model_version: Optional[str] = None
    image_quality: Optional[float] = None
    lighting_condition: Optional[str] = None


class OccupancyReadingResponse(BaseModel):
    """
    Schema for occupancy reading response.
    """
    id: str
    vehicle_id: str
    person_count: int
    occupancy_percentage: float
    confidence: float
    recorded_at: datetime
    processing_time_ms: Optional[int] = None
    edge_device_id: Optional[str] = None

    class Config:
        from_attributes = True


class OccupancyHistoryResponse(BaseModel):
    """
    Schema for occupancy history.
    """
    vehicle_id: str
    readings_count: int
    average_occupancy: float
    peak_occupancy: int
    lowest_occupancy: int
    readings: list[OccupancyReadingResponse]


class OccupancyCurrentResponse(BaseModel):
    """
    Schema for current occupancy status.
    """
    vehicle_id: str
    person_count: int
    occupancy_percentage: float
    capacity: int
    status: str
    confidence: float
    last_updated: datetime
    is_overcrowded: bool
