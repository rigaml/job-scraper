"""
Defines a job table.
"""

from datetime import datetime
from sqlalchemy import DateTime, String, Text, ForeignKey, UniqueConstraint
from sqlalchemy import func as sql_func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


class Job(Base):
    __tablename__ = "job"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    jobs_site_id: Mapped[int] = mapped_column(ForeignKey("jobs_site.id"), nullable=False)
    ref: Mapped[str] = mapped_column(String)
    title: Mapped[str] = mapped_column(String)
    salary: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    type: Mapped[str] = mapped_column(String)
    skills: Mapped[str]= mapped_column(Text, nullable=False)
    duration: Mapped[str] = mapped_column(String)
    start_date: Mapped[str] = mapped_column(String)
    rate: Mapped[str] = mapped_column(String)
    recruiter: Mapped[str] = mapped_column(String)
    posted_date: Mapped[str] = mapped_column(String)
    permalink: Mapped[str] = mapped_column(String)
    hash_key: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=sql_func.now())

    __table_args__ = (UniqueConstraint("jobs_site_id", "hash_key"),)

    # Define the relationship to JobsSite
    jobs_site = relationship("app.database.jobs_site.JobsSite", back_populates="jobs")

    def __repr__(self):
        return (
            f"Job("
            f"id= {self.id}, "
            f"jobs_site_id= {self.jobs_site_id}, "
            f"ref= {self.ref}, "
            f"title= {self.title}, "
            f"salary= {self.salary}, "
            f"location= {self.location}, "
            f"type= {self.type}, "
            f"skills= {self.skills}, "
            f"duration= {self.duration}, "
            f"start_date= {self.start_date}, "
            f"rate= {self.rate}, "
            f"recruiter= {self.recruiter}, "
            f"posted_date= {self.posted_date}, "
            f"permalink= {self.permalink}, "
            f"hash_key= {self.hash_key}, "
            f"created_at= {self.created_at}"
            ")"
        )
    

