"""
Vehicle Pydantic schemas for validation.
"""
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime


class LocationBase(BaseModel):
    """
    Base location schema.
    """
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class VehicleCreate(BaseModel):
    """
    Schema for creating a new vehicle.
    """
    registration_number: str
    vehicle_type: str = "BUS"
    capacity: int = Field(..., gt=0)
    route_id: Optional[str] = None
    route_name: Optional[str] = None
    device_id: Optional[str] = None
    max_capacity_alert_threshold: int = Field(default=85, ge=0, le=100)
    critical_alert_threshold: int = Field(default=95, ge=0, le=100)


class VehicleUpdate(BaseModel):
    """
    Schema for updating a vehicle.
    """
    registration_number: Optional[str] = None
    capacity: Optional[int] = None
    route_id: Optional[str] = None
    route_name: Optional[str] = None
    status: Optional[str] = None
    max_capacity_alert_threshold: Optional[int] = None
    critical_alert_threshold: Optional[int] = None
    notes: Optional[str] = None


class VehicleResponse(BaseModel):
    """
    Schema for vehicle response.
    """
    id: str
    registration_number: str
    vehicle_type: str
    capacity: int
    current_occupancy: int
    occupancy_percentage: Optional[float] = None
    status: str
    route_id: Optional[str] = None
    route_name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    device_id: Optional[str] = None
    last_heartbeat: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
