"""Scraper for Jobserve website"""

import logging
import time
from typing import List, Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from scrapers.jobs_scraper import JobsScraper
from models.job import Job

import utils.text_utils as text_utils
import utils.html_utils as html_utils

logger = logging.getLogger(__name__)


class JobserveScraper(JobsScraper):
    """Extract jobs from Jobserve"""

    _SITE_NAME = "jobserve"
    _JOBS_URL = "https://www.jobserve.com/gb/en/JobSearch.aspx?shid="
    # Selector list of offers
    _SEL_JOB_LIST = "#jsJobResContent .jobItem"
    # Selectors fields for each item in the list of offers
    _SEL_JOB_ITEM_TITLE = ".jobResultsTitle"
    _SEL_JOB_ITEM_SALARY = ".jobResultsSalary"
    _SEL_JOB_ITEM_LOC = ".jobResultsLoc"
    _SEL_JOB_ITEM_TYPE = ".jobResultsType"
    # Selector job details container
    _SEL_JOB_DETAIL_CONTAINER = "#JobDetailContainer .jsCustomScrollContainer"
    # Job details description
    _SEL_JOB_DETAIL_SKILLS = "#md_skills"
    _SEL_JOB_DETAIL_DURATION = "#md_duration"
    _SEL_JOB_DETAIL_START_DATE = "#md_start_date"
    _SEL_JOB_DETAIL_RATE = "#md_rate"
    _SEL_JOB_DETAIL_RECRUITER = "#md_recruiter"
    _SEL_JOB_DETAIL_REF = "#md_ref"
    _SEL_JOB_DETAIL_POSTED_DATE = "#md_posted_date"
    _SEL_JOB_DETAIL_PERMALINK = "#md_permalink"

    def __init__(self, session_id, show_browser=False):
        self.jobs_url = self._JOBS_URL + session_id
        super().__init__(self.jobs_url, show_browser)

    def get_site_name(self) -> str:
        """Returns the site name this class scrapes"""

        return self._SITE_NAME

    def scrape(self, max_jobs_retrieve: int) -> List[Job]:
        """Scrape job listings returning list of Job objects."""

        job_items = self._get_job_items(max_jobs_retrieve)

        retrieved_jobs = []
        for index, job_item in enumerate(job_items):
            logger.debug("**Job Index: %s", index + 1)
            self._click_job_item(job_item)
            current_job = self._extract_job_details(job_item)
            retrieved_jobs.append(current_job)
            logger.debug("Retrieved job: %s", current_job)

        return retrieved_jobs

    def _get_job_items(self, max_jobs_retrieve: int) -> List[WebElement]:
        """Retrieve job items from the listing page. Returns a maximum of 'retrieve_jobs_max' items."""
        try:
            job_items = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, self._SEL_JOB_LIST)))

            logger.debug("Job items found: %s and max required: %s", len(job_items), max_jobs_retrieve)

            return job_items[: min(len(job_items), max_jobs_retrieve)]
        except Exception as e:
            logger.error("Error retrieving job items: %s", e)
            return []

    def _click_job_item(self, job_element: WebElement):
        """Click on a job item to load its details."""
        try:
            ActionChains(self.driver).move_to_element(job_element).click(job_element).perform()
            time.sleep(2)
        except Exception as e:
            logger.error("Error clicking on job item: %s", e)

    def _extract_job_details(self, job_element: WebElement) -> Job:
        """Extract job details from a job item."""
        job = Job()
        job.title = html_utils.find_element_text(job_element, self._SEL_JOB_ITEM_TITLE)
        job.salary = html_utils.find_element_text(job_element, self._SEL_JOB_ITEM_SALARY)
        job.loc = html_utils.find_element_text(job_element, self._SEL_JOB_ITEM_LOC)
        job.type = html_utils.find_element_text(job_element, self._SEL_JOB_ITEM_TYPE)

        job_detail_container = self._get_job_detail_container()
        if job_detail_container:
            self._scroll_and_extract_details(job_detail_container, job)

        return job

    def _get_job_detail_container(self) -> Optional[WebElement]:
        """Retrieve the job detail container element."""
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self._SEL_JOB_DETAIL_CONTAINER)))
        except Exception as e:
            logger.error("Error retrieving job detail container: %s", e)
            return None

    def _scroll_and_extract_details(self, container: WebElement, job: Job):
        """Scroll through the job details container and extract the details."""
        try:
            scroll_height = self.driver.execute_script("return arguments[0].scrollHeight;", container)
            logger.debug("Scrolling height: %s", scroll_height)

            current_scroll_position = 0
            pixels_scroll = 100
            while current_scroll_position < scroll_height:
                self.driver.execute_script(f"arguments[0].scrollTop = {current_scroll_position};", container)
                current_scroll_position += pixels_scroll
                time.sleep(1)

                job.skills = text_utils.join_without_overlap(
                    job.skills, html_utils.find_element_text(container, self._SEL_JOB_DETAIL_SKILLS))
                job.duration = text_utils.join_without_overlap(
                    job.duration, html_utils.find_element_text(container, self._SEL_JOB_DETAIL_DURATION))
                job.start_date = text_utils.join_without_overlap(
                    job.start_date, html_utils.find_element_text(container, self._SEL_JOB_DETAIL_START_DATE)
                )
                job.rate = text_utils.join_without_overlap(
                    job.rate, html_utils.find_element_text(container, self._SEL_JOB_DETAIL_RATE))
                job.recruiter = text_utils.join_without_overlap(
                    job.recruiter, html_utils.find_element_text(container, self._SEL_JOB_DETAIL_RECRUITER)
                )
                job.ref = text_utils.join_without_overlap(
                    job.ref, html_utils.find_element_text(container, self._SEL_JOB_DETAIL_REF))
                job.posted_date = text_utils.join_without_overlap(
                    job.posted_date, html_utils.find_element_text(container, self._SEL_JOB_DETAIL_POSTED_DATE)
                )
                job.permalink = text_utils.join_without_overlap(
                    job.permalink, html_utils.find_element_text(container, self._SEL_JOB_DETAIL_PERMALINK)
                )

        except Exception as e:
            logger.error("Error during scrolling and extracting details: %s", e)
