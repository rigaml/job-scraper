"""
Script to initialize an empty database

File should have import of table definitions on top for SQLAlchemy 
to be able to create the tables. That is import database.job, import database.jobs_site...
"""
import os
import sys
import utils.file_utils as fu
import settings
import database.database as db

from database.job import Job
from database.jobs_site import JobsSite

from database.jobs_site_repository import JobsSiteRepository

if __name__ == "__main__":

    absolute_path_database = fu.get_absolute_path_file(settings.JOBS_DATABASE_PATH_NAME)
    if os.path.exists(absolute_path_database):
        print((f"Database already exist at: {absolute_path_database}."
               "Remove if want to create an empty one."))
        sys.exit()

    jobs_db = db.Database(f"sqlite:///{absolute_path_database}")
    jobs_db.create_database()

    print("Database created at: ", absolute_path_database)

    jobs_site_repo = JobsSiteRepository(jobs_db.session)
    jobs_site = jobs_site_repo.add("jobserve", "https://www.jobserve.com")

    print("Jobs site created", jobs_site)
