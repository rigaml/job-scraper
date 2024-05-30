"""
Abstract class that defines common methods that scrapers for different jobs sites should implement.
"""

from abc import ABC, abstractmethod
from typing import List

from database.job import Job
from scrapers.scrapper_context_manager import ScrapperContextManager


class JobsScraper(ScrapperContextManager, ABC):

    @abstractmethod
    def get_site_name(self) -> str:
        """
        Returns the name of the site this class is scraping jobs from.
        """
        pass

    @abstractmethod
    def scrape(self, retrieve_jobs_max: int) -> List[Job]:
        """
        Implement method to scrape jobs
        """
        pass
