"""
Script to initialize an empty database

File should have import of table definitions on top for SQLAlchemy 
to be able to create the tables. That is import database.job, import database.jobs_site...
"""

import os
import sys

import app.settings as settings
from app.database.database import Database

from database.jobs_site_repository import JobsSiteRepository

if __name__ == "__main__":

    database_path_name = settings.JOBS_DATABASE_PATH_NAME
    if os.path.exists(database_path_name):
        print((f"Database already exist at: {database_path_name}." "Remove if want to create an empty one."))
        sys.exit()

    jobs_db = Database(f"sqlite:///{database_path_name}")
    jobs_db.create_database()

    print("Database created at: ", database_path_name)

    jobs_site_repo = JobsSiteRepository(jobs_db)
    jobs_site = jobs_site_repo.add("jobserve", "https://www.jobserve.com")

    print("Jobs site created", jobs_site)
