"""Models module."""

from sqlalchemy import Column, String, Boolean, Integer

from .database import Base


class JobSite(Base):

    # SQLite convention for table names: use snake_case for table names and singular nouns.
    __tablename__ = "job_site"

    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"id: {self.id}\n" \
               f"url: {self.url}\n" \
               f"is_active: {self.is_active}"