"""
Job scraped from the website.
"""

from dataclasses import dataclass
from app.database.job import Job


@dataclass
class JobDTO:
    """
    Job Data Transfer Object
    """
    ref: str = ""
    title: str = ""
    salary: str = ""
    loc: str = ""
    type: str = ""
    skills: str = ""
    duration: str = ""
    start_date: str = ""
    rate: str = ""
    recruiter: str = ""
    posted_date: str = ""
    permalink: str = ""

    @classmethod
    def create_from_db(cls, job: Job) -> 'JobDTO':
        return cls(job.ref, job.title, job.salary, job.location, job.type, job.skills, job.duration,
                   job.start_date, job.rate, job.recruiter, job.posted_date, job.permalink)
