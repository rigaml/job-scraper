"""
Scrapes jobs from the specified jobs site and stores them in the database.
    +Jobs database should exist in: ../data/job-scrape.db  (to create a new one use 'app/scripts/create_database.py')
    +Logs folder should exist in: ../logs
"""

import json
import sys
import time
import logging
import logging.config

from injector import Injector

import app.settings as settings
from app.dependency_module import DependencyModule

from app.scrapers.jobs_scraper import JobsScraper
from app.scrapers.jobserve_scraper import JobserveScraper

from app.database.database import Database
from app.database.job import Job
from app.database.job_repository import JobRepository
from app.database.jobs_site_repository import JobsSiteRepository

import utils.text_utils as tu


def init_logger(config_path="app/logging_config.json"):
    """
    Initialize and return the module logger.
    """
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
        logging.config.dictConfig(config)

    return logging.getLogger(__name__)


logger = init_logger()


def scrape_jobs(scraper: JobsScraper, jobs_site_id: int, job_repo: JobRepository):
    """
    Scrape jobs and store them in the repository.
    """
    with scraper as scraper_instance:
        try:
            web_jobs = scraper_instance.scrape(settings.SCRAPE_RETRIEVE_MAX)
        except Exception as e:
            logger.error("Error during scraping: %s", e)
            return

        if settings.SCRAPE_SHOW_BROWSER:
            time.sleep(10)

    for web_job in web_jobs:
        store_jobs(web_job, jobs_site_id, job_repo)


def store_jobs(job: Job, jobs_site_id: int, job_repo: JobRepository):
    """
    Stores the job in the repository.
    """
    if not job.skills:
        logger.error("Could not retrieve skills from job site: %s", job)
        return

    job_hash_key = tu.generate_hash_key(job.skills)
    db_job = job_repo.get_by_hash_key(jobs_site_id, job_hash_key)

    if db_job:
        logger.info("Job already in database: %s", db_job)
    else:
        db_job = Job(
            jobs_site_id=jobs_site_id,
            ref=job.ref,
            title=job.title,
            salary=job.salary,
            location=job.loc,
            type=job.type,
            skills=job.skills,
            duration=job.duration,
            start_date=job.start_date,
            rate=job.rate,
            recruiter=job.recruiter,
            posted_date=job.posted_date,
            hash_key=job_hash_key,
            permalink=job.permalink,
        )
        job_repo.add(db_job)


def setup_database(jobs_db: Database):
    """
    Setup and return the database connection and repositories.
    """
    jobs_site_repo = JobsSiteRepository(jobs_db)
    job_repository = JobRepository(jobs_db)

    return jobs_site_repo, job_repository


def main():
    """
    Main function to run the job scraper.
    """

    injector = Injector([DependencyModule()])

    jobs_site_repo, job_repository = setup_database(injector.get(Database))

    jobs_site = jobs_site_repo.get_by_name(settings.SCRAPE_SITE)
    if not jobs_site:
        logger.error("Jobs site %s not found in database.", settings.SCRAPE_SITE)
        sys.exit()

    jobserve_session_id = settings.get_secret(settings.SCRAPE_SITE + "-shid")
    jobserve_scraper = JobserveScraper(jobserve_session_id, settings.SCRAPE_SHOW_BROWSER)

    scrape_jobs(jobserve_scraper, jobs_site.id, job_repository)
    logger.info("Scraping ended")


if __name__ == "__main__":
    main()
