from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base

class JobSite(Base):
    __tablename__ = "job_site"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    url: Mapped[str] = mapped_column(String, unique=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # Optional: Define the relationship to User
    jobs = relationship("User", back_populates="job_site")

    def __repr__(self):
        return f"id: {self.id}\n" \
               f"url: {self.url}\n" \
               f"is_active: {self.is_active}"