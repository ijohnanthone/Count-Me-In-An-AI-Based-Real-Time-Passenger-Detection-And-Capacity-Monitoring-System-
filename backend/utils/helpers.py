"""
Helper utility functions.
"""
import uuid
from datetime import datetime


def generate_id() -> str:
    """
    Generate a unique ID.
    """
    return str(uuid.uuid4())


def get_current_timestamp() -> datetime:
    """
    Get current UTC timestamp.
    """
    return datetime.utcnow()


def calculate_percentage(value: float, total: float) -> float:
    """
    Calculate percentage safely.
    """
    if total <= 0:
        return 0.0
    return (value / total) * 100
