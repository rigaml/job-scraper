"""
Defines a jobs site.
"""

from datetime import datetime
from sqlalchemy import String, Boolean
from sqlalchemy import func as sql_func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base


class JobsSite(Base):
    __tablename__ = "jobs_site"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    site_name: Mapped[str] = mapped_column(String, unique=True)
    url: Mapped[str] = mapped_column(String, unique=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(server_default=sql_func.now())

    # Optional: Define the relationship to User
    jobs = relationship("Job", back_populates="jobs_site")

    def __repr__(self):
        return (
            f"JobsSite(id= {self.id}, "
            f"site_name= {self.site_name}, "
            f"url= {self.url}, "
            f"is_active= {self.is_active}, "
            f"created_at= {self.created_at})"
        )
