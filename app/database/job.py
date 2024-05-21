"""
Defines a job table.
"""
from datetime import datetime
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy import func as sql_func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base


class Job(Base):
    __tablename__ = "job"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    jobs_site_id: Mapped[int] = mapped_column(ForeignKey("jobs_site.id"), nullable=False)
    ref: Mapped[str]
    title: Mapped[str]
    salary: Mapped[str]
    location: Mapped[str]
    type: Mapped[str]
    skills: Mapped[str]
    duration: Mapped[str]
    start_date: Mapped[str]
    rate: Mapped[str]
    recruiter: Mapped[str]
    posted_date: Mapped[str]
    permalink: Mapped[str]
    hash_key: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=sql_func.now())

    __table_args__ = (
        UniqueConstraint("jobs_site_id", "hash_key"),
    )

    jobs_site = relationship("JobsSite", back_populates="jobs")

    def __str__(self):
        return (
            f"Job(id= {self.id}, "
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
            f"created_at= {self.created_at})"
        )
