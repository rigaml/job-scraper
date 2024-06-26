from typing import List
import pytest

from app.database.job import Job
from app.scrapers.jobs_scraper import JobsScraper

class TestJobsScraper(JobsScraper):
    def get_site_name(self) -> str:
        return "TestSite"
    
    def scrape(self, retrieve_jobs_max: int) -> List[Job]:
        return [Job(id=i, title=f"Job{i}", salary=f"Salary{i}", location=f"Location{i}") for i in range(retrieve_jobs_max)]

@pytest.fixture
def scraper():
    return TestJobsScraper("http://example.com", False)

def test_get_site_name_returns_correct_name(scraper):
    assert scraper.get_site_name() == "TestSite"

def test_scrape_returns_correct_number_of_jobs(scraper):
    max_jobs = 5
    
    jobs = scraper.scrape(max_jobs)
    
    assert len(jobs) == max_jobs
    for i, job in enumerate(jobs):
        assert job.id == i
        assert job.title == f"Job{i}"
        assert job.salary == f"Salary{i}"
        assert job.location == f"Location{i}"