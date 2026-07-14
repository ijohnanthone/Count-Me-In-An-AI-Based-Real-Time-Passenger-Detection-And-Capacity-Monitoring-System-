"""
Alert model for storing system alerts.
"""
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey, Index, DateTime, Enum
from enum import Enum as PyEnum
from datetime import datetime
from database.models.base import BaseModel


class AlertType(str, PyEnum):
    """Types of alerts in the system."""
    CAPACITY_HIGH = "CAPACITY_HIGH"
    CAPACITY_CRITICAL = "CAPACITY_CRITICAL"
    DEVICE_OFFLINE = "DEVICE_OFFLINE"
    INFERENCE_FAILED = "INFERENCE_FAILED"
    UNUSUAL_PATTERN = "UNUSUAL_PATTERN"
    SENSOR_ERROR = "SENSOR_ERROR"


class AlertSeverity(str, PyEnum):
    """Severity levels for alerts."""
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class Alert(BaseModel):
    """
    Alert model storing system alerts and notifications.
    """
    __tablename__ = "alerts"

    id = Column(String(36), primary_key=True, index=True)
    vehicle_id = Column(
        String(36),
        ForeignKey("vehicles.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    
    # Alert Information
    alert_type = Column(String(50), nullable=False, index=True)
    severity = Column(String(20), default=AlertSeverity.MEDIUM, nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(String(1000))
    
    # Data
    occupancy_percentage = Column(Float, nullable=True)
    person_count = Column(Integer, nullable=True)
    threshold_value = Column(Float, nullable=True)
    
    # Status
    is_active = Column(Boolean, default=True, nullable=False, index=True)
    acknowledged = Column(Boolean, default=False, nullable=False)
    acknowledged_by = Column(String(36), nullable=True)
    acknowledged_at = Column(DateTime, nullable=True)
    
    # Timing
    triggered_at = Column(
        DateTime,
        nullable=False,
        index=True,
        default=datetime.utcnow,
    )
    resolved_at = Column(DateTime, nullable=True)
    
    # Metadata
    notes = Column(String(1000))
    notification_sent = Column(Boolean, default=False)
    webhook_delivered = Column(Boolean, default=False)

    __table_args__ = (
        Index("idx_alert_vehicle_time", "vehicle_id", "triggered_at"),
        Index("idx_alert_status", "is_active", "acknowledged"),
        Index("idx_alert_severity", "severity"),
        Index("idx_alert_type", "alert_type"),
    )

    def __repr__(self):
        return f"<Alert(id={self.id}, vehicle_id={self.vehicle_id}, type={self.alert_type}, severity={self.severity})>"
