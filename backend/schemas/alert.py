"""
Alert Pydantic schemas for validation.
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class AlertCreate(BaseModel):
    """
    Schema for creating an alert.
    """
    vehicle_id: str
    alert_type: str
    severity: str = "MEDIUM"
    title: str
    description: Optional[str] = None
    occupancy_percentage: Optional[float] = None
    person_count: Optional[int] = None


class AlertAcknowledge(BaseModel):
    """
    Schema for acknowledging an alert.
    """
    acknowledged_by: str
    notes: Optional[str] = None


class AlertResponse(BaseModel):
    """
    Schema for alert response.
    """
    id: str
    vehicle_id: str
    alert_type: str
    severity: str
    title: str
    description: Optional[str] = None
    is_active: bool
    acknowledged: bool
    acknowledged_by: Optional[str] = None
    acknowledged_at: Optional[datetime] = None
    triggered_at: datetime
    created_at: datetime

    class Config:
        from_attributes = True
