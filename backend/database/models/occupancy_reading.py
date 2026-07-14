"""
Occupancy Reading model for storing person count data.
"""
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Index, JSON, DateTime
from datetime import datetime
from database.models.base import BaseModel


class OccupancyReading(BaseModel):
    """
    Occupancy Reading model storing person count data from edge devices.
    """
    __tablename__ = "occupancy_readings"

    id = Column(String(36), primary_key=True, index=True)
    vehicle_id = Column(
        String(36),
        ForeignKey("vehicles.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    
    # Detection Data
    person_count = Column(Integer, nullable=False)
    occupancy_percentage = Column(Float, nullable=False)
    confidence = Column(Float, default=0.0)  # Model confidence score
    
    # Timing
    recorded_at = Column(
        DateTime,
        nullable=False,
        index=True,
        default=datetime.utcnow,
    )
    processing_time_ms = Column(Integer)  # Time taken for inference
    
    # Additional Data
    frame_data = Column(JSON)  # Store frame metadata or base64 thumbnail
    edge_device_id = Column(String(100), nullable=True, index=True)
    model_version = Column(String(50), nullable=True)
    
    # Quality Metrics
    image_quality = Column(Float, nullable=True)  # 0-1 scale
    lighting_condition = Column(String(50), nullable=True)  # GOOD, POOR, etc.
    occlusion_level = Column(Float, nullable=True)  # 0-1 scale

    __table_args__ = (
        Index("idx_occupancy_vehicle_time", "vehicle_id", "recorded_at"),
        Index("idx_occupancy_recorded", "recorded_at"),
        Index("idx_occupancy_device", "edge_device_id"),
    )

    def __repr__(self):
        return f"<OccupancyReading(id={self.id}, vehicle_id={self.vehicle_id}, person_count={self.person_count})>"
