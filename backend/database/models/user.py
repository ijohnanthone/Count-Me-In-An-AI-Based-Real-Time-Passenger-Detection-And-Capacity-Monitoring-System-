"""
User model for authentication and authorization.
"""
from sqlalchemy import Column, String, Enum, Boolean, Index
from enum import Enum as PyEnum
from database.models.base import BaseModel


class UserRole(str, PyEnum):
    """User roles for RBAC."""
    ADMIN = "ADMIN"
    OPERATOR = "OPERATOR"
    VIEWER = "VIEWER"
    COMMUTER = "COMMUTER"


class User(BaseModel):
    """
    User model for authentication.
    """
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    full_name = Column(String(255))
    password_hash = Column(String(255), nullable=False)
    role = Column(String(50), default=UserRole.VIEWER, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)

    __table_args__ = (
        Index("idx_user_email", "email"),
        Index("idx_user_role", "role"),
    )

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, role={self.role})>"
