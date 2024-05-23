"""
Jobs site repository
Identifies a source of jobs to scrape.
"""

from typing import Callable, ContextManager, Optional
from sqlalchemy.orm import Session

from database.jobs_site import JobsSite


class JobsSiteRepository:

    def __init__(self, session_factory: Callable[..., ContextManager[Session]]):
        self.session_factory = session_factory

    def get_by_name(self, site_name: str) -> Optional[JobsSite]:
        with self.session_factory() as session:
            return session.query(JobsSite).filter(JobsSite.site_name == site_name).one_or_none()

    def add(self, site_name: str, url: str, is_active: bool = True) -> JobsSite:
        jobs_site = JobsSite(site_name=site_name, url=url, is_active=is_active)
        with self.session_factory() as session:
            session.add(jobs_site)
            session.commit()
            session.refresh(jobs_site)
            return jobs_site
