"""
Jobs site repository
Identifies a source of jobs to scrape.
"""

from typing import Optional, List

from app.database.database import Database
from app.database.jobs_site import JobsSite


class JobsSiteRepository:

    def __init__(self, database: Database):
        self.session_factory = database.session

    def get_by_name(self, site_name: str) -> Optional[JobsSite]:
        with self.session_factory() as session:
            return session.query(JobsSite).filter(JobsSite.site_name == site_name).one_or_none()

    def get_jobs_sites(self, skip: int = 0, limit: int = 10) -> List[JobsSite]:
        with self.session_factory() as session:
            return session.query(JobsSite).offset(skip).limit(limit).all()

    def add(self, site_name: str, url: str, is_active: bool = True) -> JobsSite:
        jobs_site = JobsSite(site_name=site_name, url=url, is_active=is_active)
        with self.session_factory() as session:
            session.add(jobs_site)
            session.commit()
            session.refresh(jobs_site)
            return jobs_site
