from app.db.models.base import Base
from datetime import datetime, timezone
from sqlalchemy import String, Enum, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column
import enum
from sqlalchemy import Uuid
import uuid


class ReportType(enum.Enum):
    CHURN = "churn"
    REVENUE = "revenue"
    INCIDENT_SUMARY = "incident_summary"
    KPI_WEEKLY = "kpi_weekly"


class Status(enum.Enum):
    PENDING = "pending"
    GENERATING = "generating"
    COMPLETED = "completed"
    FAILED = "failed"


class Report(Base):
    __tablename__ = "report"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(50))
    report_type: Mapped[ReportType] = mapped_column(Enum(ReportType))
    status: Mapped[Status] = mapped_column(Enum(Status))
    content: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    period_start: Mapped[datetime] = mapped_column(DateTime)
    period_end: Mapped[datetime] = mapped_column(DateTime)
    requested_by: Mapped[str] = mapped_column(String(40))
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )
    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime, default=datetime.now(timezone.utc), nullable=True
    )
