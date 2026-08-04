from sqlalchemy import Column, Integer, String

from app.core.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    resumes = relationship(
    "Resume",
    back_populates="user",
    cascade="all, delete"
        )
    chat_sessions = relationship(
    "ChatSession",
    back_populates="user",
    cascade="all, delete-orphan"
    )
    notifications = relationship(
    "Notification",
    back_populates="user",
    cascade="all, delete-orphan"
    )

