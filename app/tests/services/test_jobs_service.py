

from unittest.mock import Mock

import pytest

import copy

from app.database.job import Job
from app.database.job_repository import JobRepository
from app.services.job_dto import JobDTO
from app.services.jobs_service import JobsService

expected = [Job(id=1, jobs_site_id=1, title="job1"), Job(id=2, jobs_site_id=1, title="job2")]

@pytest.fixture
def job_repository():
    mock_job_repository= Mock(spec=JobRepository)
    mock_job_repository.get_jobs.return_value = expected
    return mock_job_repository

def test_get_jobs(job_repository):
    service = JobsService(job_repository)

    result = service.get_jobs(0, 2)
    expected_jobs= [JobDTO.create_from_db(job) for job in expected]
    result = copy.deepcopy(expected_jobs)

    assert all(a == b for a, b in zip(result, expected_jobs))
