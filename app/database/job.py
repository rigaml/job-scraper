from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base

class User(Base):
    __tablename__ = "job"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    job_site_id: Mapped[int] = mapped_column(ForeignKey("job_site.id"), nullable=False)
    ref: Mapped[str]
    title: Mapped[str]
    salary: Mapped[int]
    location: Mapped[str]
    type: Mapped[str]
    when: Mapped[str]
    skills: Mapped[str]
    duration: Mapped[str]
    start_date: Mapped[str]
    rate: Mapped[str]
    recruiter: Mapped[str]
    posted_date: Mapped[str]
    permalink: Mapped[str]

    __table_args__ = (
        UniqueConstraint("job_site_id", "ref"),
    )

    job_site = relationship("JobSite", back_populates="jobs")

    def __str__(self):
        return (
            f"Id: {self.id}\n"
            f"Job Site Id: {self.job_site_id}\n"
            f"Reference: {self.ref}\n"
            f"Job Title: {self.title}\n"
            f"Salary: {self.salary}\n"
            f"Location: {self.location}\n"
            f"Type: {self.type}\n"
            f"When: {self.when}\n"
            f"Skills: {self.skills}\n"
            f"Duration: {self.duration}\n"
            f"Start Date: {self.start_date}\n"
            f"Rate: {self.rate}\n"
            f"Recruiter: {self.recruiter}\n"
            f"Posted Date: {self.posted_date}\n"
            f"Permalink: {self.permalink}"
        )