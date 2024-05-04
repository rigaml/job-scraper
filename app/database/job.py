"""Models module."""

from sqlalchemy import Column, ForeignKey, UniqueConstraint, String, Integer

from .database import Base


class User(Base):

    __tablename__ = "job"

    id = Column(Integer, primary_key=True)
    job_site_id = Column(Integer, ForeignKey("job_site.id"))

    ref = Column(String)
    title = Column(String)
    salary = Column(Integer)
    location = Column(String)
    type = Column(String)
    when = Column(String)
    skills = Column(String)
    duration = Column(String)
    start_date = Column(String)
    rate = Column(String)
    recruiter = Column(String)
    posted_date = Column(String)
    permalink = Column(String)
    
    __table_args__ = (
        UniqueConstraint("job_site_id", "ref"),
    )

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