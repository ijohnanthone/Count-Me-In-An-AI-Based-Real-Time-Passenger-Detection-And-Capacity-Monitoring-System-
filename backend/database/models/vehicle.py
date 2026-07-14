"""
Vehicle model for storing vehicle information.
"""
from sqlalchemy import Column, String, Integer, Float, Enum, Index, JSON
from enum import Enum as PyEnum
from database.models.base import BaseModel


class VehicleStatus(str, PyEnum):
    """Vehicle operational status."""
    OPERATIONAL = "OPERATIONAL"
    MAINTENANCE = "MAINTENANCE"
    OFFLINE = "OFFLINE"
    INACTIVE = "INACTIVE"


class Vehicle(BaseModel):
    """
    Vehicle model storing information about each vehicle.
    """
    __tablename__ = "vehicles"

    id = Column(String(36), primary_key=True, index=True)
    registration_number = Column(String(50), unique=True, nullable=False, index=True)
    vehicle_type = Column(String(100), default="BUS")  # BUS, TRAIN, METRO, etc.
    capacity = Column(Integer, nullable=False)
    current_occupancy = Column(Integer, default=0)
    status = Column(String(50), default=VehicleStatus.OPERATIONAL, nullable=False)
    route_id = Column(String(36), index=True)
    route_name = Column(String(255))
    
    # Location
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    
    # Device Information
    device_id = Column(String(100), unique=True, nullable=True, index=True)
    device_ip = Column(String(45), nullable=True)  # IPv4 or IPv6
    last_heartbeat = Column(String(50), nullable=True)
    
    # Configuration
    max_capacity_alert_threshold = Column(Integer, default=85)  # Percentage
    critical_alert_threshold = Column(Integer, default=95)  # Percentage
    camera_config = Column(JSON)  # Store camera settings as JSON
    
    # Metadata
    notes = Column(String(500))
    operator_id = Column(String(36), nullable=True, index=True)

    __table_args__ = (
        Index("idx_vehicle_registration", "registration_number"),
        Index("idx_vehicle_route", "route_id"),
        Index("idx_vehicle_status", "status"),
        Index("idx_vehicle_device", "device_id"),
    )

    def __repr__(self):
        return f"<Vehicle(id={self.id}, registration={self.registration_number}, capacity={self.capacity})>"
