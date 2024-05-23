"""
Scrapes jobs from the specified jobs site and stores them in the database.
    +Jobs database should exist in: ../data/job-scrape.db  (to create a new one use 'app/scripts/create_database.py')
    +Logs folder should exist in: ../logs
"""

import json
import os
import sys
import time
import logging
import logging.config

import settings

from scrapers.jobs_scraper import JobsScraper
from scrapers.jobserve_scraper import JobserveScraper

import database.database as db
from database.job import Job
from database.job_repository import JobRepository
from database.jobs_site_repository import JobsSiteRepository

import utils.file_utils as fu
import utils.text_utils as tu


def init_logger():
    """Initialize and return the module logger."""
    return logging.getLogger(__name__)


logger = init_logger()


def load_logging_config(config_path="logging_config.json"):
    """Load logging configuration from a JSON file."""
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
        logging.config.dictConfig(config)


def scrape_jobs(scraper: JobsScraper, jobs_site_id: int, job_repo: JobRepository):
    """Scrape jobs and store them in the repository."""
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
    """Stores the job in the repository."""
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


def setup_database():
    """Setup and return the database connection and repositories."""
    absolute_path_database = fu.get_absolute_path_in_parent(settings.JOBS_DATABASE_PATH_NAME)
    if not os.path.exists(absolute_path_database):
        logger.error("Database doesn't exist at location: %s", absolute_path_database)
        sys.exit()

    jobs_db = db.Database(f"sqlite:///{absolute_path_database}")
    jobs_site_repo = JobsSiteRepository(jobs_db.session)
    job_repository = JobRepository(jobs_db.session)

    return jobs_site_repo, job_repository


def main():
    """Main function to run the job scraper."""
    load_logging_config()

    jobs_site_repo, job_repository = setup_database()

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
