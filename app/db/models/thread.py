from app.db.models.base import Base
from datetime import datetime, timezone
from sqlalchemy import String, Enum, DateTime, JSON, Boolean
from sqlalchemy.orm import Mapped, mapped_column
import enum
from sqlalchemy import Uuid
import uuid


class Status(enum.Enum):
    ACTIVE = "active"
    WAITING_HUMAN = "waiting_for_human"
    COMPLETED = "completed"
    ERROR = "error"


class Agent(enum.Enum):
    SUPERVISOR = "supervisor"
    ANALYTICS = "analytics"
    INCIDENTS = "incidents"
    REPORTS = "reports"


class Thread(Base):
    __tablename__ = "thread"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    user_id: Mapped[str] = mapped_column(String(50))
    status: Mapped[Status] = mapped_column(Enum(Status))
    active_agent: Mapped[Agent] = mapped_column(Enum(Agent))
    hitl_pending: Mapped[bool] = mapped_column(Boolean, default=False)
    hitl_action: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )
    last_message_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )
