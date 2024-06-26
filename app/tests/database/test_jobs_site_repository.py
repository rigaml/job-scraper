import site
import pytest
from unittest.mock import MagicMock
from app.database.jobs_site import JobsSite
from app.database.database import Database
from app.database.jobs_site_repository import JobsSiteRepository

@pytest.fixture
def mock_database():
    return MagicMock(spec=Database)

@pytest.fixture
def jobs_site_repository(mock_database):
    return JobsSiteRepository(mock_database)

def test_get_by_name(jobs_site_repository, mock_database):
    mock_session = MagicMock()
    mock_database.session.return_value.__enter__.return_value = mock_session

    mock_jobs_site = MagicMock(spec=JobsSite)
    mock_query = mock_session.query.return_value
    mock_query.filter.return_value.one_or_none.return_value = mock_jobs_site
    site_name= "example_site"

    result = jobs_site_repository.get_by_name(site_name)
    
    mock_session.query.assert_called_once_with(JobsSite)
    args, kwargs = mock_query.filter.call_args
    assert str(args[0]) == str(JobsSite.site_name == site_name)
    mock_query.filter.return_value.one_or_none.assert_called_once()
    assert result == mock_jobs_site

def test_get_jobs_sites(jobs_site_repository, mock_database):
    mock_session = MagicMock()
    mock_database.session.return_value.__enter__.return_value = mock_session
    mock_jobs_sites = [MagicMock(spec=JobsSite), MagicMock(spec=JobsSite)]
    mock_session.query.return_value.offset.return_value.limit.return_value.all.return_value = mock_jobs_sites

    result = jobs_site_repository.get_jobs_sites(0, 2)
    
    mock_session.query.assert_called_once()
    mock_session.query.return_value.offset.assert_called_once_with(0)
    mock_session.query.return_value.offset.return_value.limit.assert_called_once_with(2)
    assert result == mock_jobs_sites

def test_add(jobs_site_repository, mock_database):
    mock_session = MagicMock()
    mock_database.session.return_value.__enter__.return_value = mock_session

    result = jobs_site_repository.add("example_site", "http://example.com", True)
    
    assert isinstance(result, JobsSite)
    mock_session.add.assert_called_once_with(result)
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once_with(result)
    assert result.site_name == "example_site"
    assert result.url == "http://example.com"
    assert result.is_active is True
