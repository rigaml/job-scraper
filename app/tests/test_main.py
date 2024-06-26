import pytest
from unittest.mock import Mock
from fastapi.testclient import TestClient

from app.main import app, injector
from app.services.jobs_service import JobsServiceBase
from app.api.job_response import JobResponse
from app.tests.test_helpers.fake_creator import generate_job_dtos

client = TestClient(app)

@pytest.fixture()
def mock_jobs_service():
    jobs_service_mock = Mock(spec=JobsServiceBase)
    
    jobs_service_mock.get_jobs.return_value = generate_job_dtos(2)
    
    injector.binder.bind(JobsServiceBase, to=jobs_service_mock, scope=None)
    
    return jobs_service_mock

def test_health_when_called_returns_ok():
    response = client.get(f"/")

    assert response.status_code == 200
    assert response.json() == {"health_check": "OK"}

def test_get_jobs_when_called_returns_response(mock_jobs_service):
    skip = 5
    limit = 7

    response = client.get(f"/jobs/?skip={skip}&limit={limit}")

    mock_jobs_service.get_jobs.assert_called_once_with(skip, limit)

    assert response.status_code == 200
    assert response.json() == [JobResponse.create_from_dto(job).model_dump() for job in mock_jobs_service.get_jobs.return_value]
