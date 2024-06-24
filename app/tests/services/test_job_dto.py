import pytest

from app.database.job import Job
from app.services.job_dto import JobDTO


def test_individual_fields():
    job_dto = JobDTO(ref="001", title="Software Engineer", salary="100000", loc="New York", type="Full-time",
                     skills="Python, Django", duration="Permanent", start_date="2024-06-01", rate="Hourly",
                     recruiter="Tech Recruiter", posted_date="2024-05-30", permalink="http://example.com/job/001")

    assert job_dto.ref == "001"
    assert job_dto.title == "Software Engineer"
    assert job_dto.salary == "100000"
    assert job_dto.loc == "New York"
    assert job_dto.type == "Full-time"
    assert job_dto.skills == "Python, Django"
    assert job_dto.duration == "Permanent"
    assert job_dto.start_date == "2024-06-01"
    assert job_dto.rate == "Hourly"
    assert job_dto.recruiter == "Tech Recruiter"
    assert job_dto.posted_date == "2024-05-30"
    assert job_dto.permalink == "http://example.com/job/001"


def test_create_from_db():
    job = Job(ref="002", title="Data Scientist", salary="120000", location="San Francisco", type="Full-time",
              skills="Python, Machine Learning", duration="Permanent", start_date="2024-07-01", rate="Annual",
              recruiter="Data Recruiter", posted_date="2024-05-31", permalink="http://example.com/job/002")
    job_dto = JobDTO.create_from_db(job)

    assert job_dto.ref == job.ref
    assert job_dto.title == job.title
    assert job_dto.salary == job.salary
    assert job_dto.loc == job.location
    assert job_dto.type == job.type
    assert job_dto.skills == job.skills
    assert job_dto.duration == job.duration
    assert job_dto.start_date == job.start_date
    assert job_dto.rate == job.rate
    assert job_dto.recruiter == job.recruiter
    assert job_dto.posted_date == job.posted_date
    assert job_dto.permalink == job.permalink
