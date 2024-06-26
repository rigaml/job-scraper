import pytest
from unittest.mock import MagicMock

from sqlalchemy import and_
from app.database.job import Job
from app.database.database import Database
from app.database.job_repository import JobRepository

@pytest.fixture
def mock_database():
    return MagicMock(spec=Database)

@pytest.fixture
def job_repository(mock_database):
    return JobRepository(mock_database)

def test_get_by_hash_key(job_repository, mock_database):
    mock_session = MagicMock()
    mock_database.session.return_value.__enter__.return_value = mock_session
    mock_job = MagicMock(spec=Job)
    mock_session.query.return_value.filter.return_value.one_or_none.return_value = mock_job
    jobs_site_id=1
    hash_key="hash123"

    result = job_repository.get_by_hash_key(jobs_site_id, hash_key)
    
    mock_session.query.assert_called_once()
    args, kwargs = mock_session.query.return_value.filter.call_args
    assert str(args[0]) == str(and_(Job.jobs_site_id == jobs_site_id, Job.hash_key == hash_key))
    
    mock_session.query.return_value.filter.assert_called_once()
    assert result == mock_job

def test_get_jobs(job_repository, mock_database):
    mock_session = MagicMock()
    mock_database.session.return_value.__enter__.return_value = mock_session
    mock_jobs = [MagicMock(spec=Job), MagicMock(spec=Job)]
    mock_session.query.return_value.offset.return_value.limit.return_value.all.return_value = mock_jobs

    result = job_repository.get_jobs(0, 2)
    
    mock_session.query.assert_called_once()
    mock_session.query.return_value.offset.assert_called_once_with(0)
    mock_session.query.return_value.offset.return_value.limit.assert_called_once_with(2)
    assert result == mock_jobs

def test_add(job_repository, mock_database):
    mock_session = MagicMock()
    mock_database.session.return_value.__enter__.return_value = mock_session
    mock_job = MagicMock(spec=Job)

    result = job_repository.add(mock_job)
    
    mock_session.add.assert_called_once_with(mock_job)
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once_with(mock_job)
    assert result == mock_job
