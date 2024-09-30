from datetime import datetime, timezone

from sqlalchemy import TIMESTAMP, Column


def get_created_at(context):
    return context.get_current_parameters()["created_at"]


class TimestampMixin(object):
    created_at = Column(
        TIMESTAMP(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False
    )
    updated_at = Column(
        TIMESTAMP(timezone=True),
        default=get_created_at,
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    deleted_at = Column(
        TIMESTAMP(timezone=True),
        default=None,
        nullable=True,
    )

    def soft_delete(self):
        self.deleted_at = datetime.now(timezone.utc)
