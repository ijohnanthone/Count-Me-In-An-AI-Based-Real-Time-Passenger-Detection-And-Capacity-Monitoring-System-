"""
Base model with common fields.
"""
from datetime import datetime
from sqlalchemy import Column, DateTime
from database.db import Base


class BaseModel(Base):
    """
    Base model with common fields for all models.
    """
    __abstract__ = True

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        index=True,
    )
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )
