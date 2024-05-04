import time

import settings as settings
import  database.database as db
import scrapers.jobserve_scraper as scraper

SHOW_BROWSER = False
RETRIEVE_JOBS_MAX = 3

def scrape_jobs(database):
    session_id = settings.get_secret("jobserve-shid")
    with scraper.JobServeScraper(session_id, SHOW_BROWSER) as scraper_instance:
        retrieved_jobs= scraper_instance.scrape_jobs(RETRIEVE_JOBS_MAX)

    if SHOW_BROWSER:
        time.sleep(10)

    print("\n\n".join([str(job) for job in retrieved_jobs]))

if __name__ == "__main__":
    database = db.Database(f"sqlite:///data/{settings.JOBS_DATABASE_NAME}.db")
    database.create_database()

    scrape_jobs(database)
    print("Scrapping Ended")
