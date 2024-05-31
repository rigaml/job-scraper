"""
Jobs repository
"""

from typing import Callable, ContextManager, List, Optional
from sqlalchemy import and_
from sqlalchemy.orm import Session

from database.job import Job


class JobRepository:

    def __init__(self, session_factory: Callable[..., ContextManager[Session]]):
        self.session_factory = session_factory

    def get_by_hash_key(self, jobs_site_id: int, hash_key: str) -> Optional[Job]:
        with self.session_factory() as session:
            return session.query(Job).filter(and_(Job.jobs_site_id == jobs_site_id, Job.hash_key == hash_key)).one_or_none()

    def get_jobs(self, skip: int = 0, limit: int = 0) -> List[Job]:
        with self.session_factory() as session:
            return session.query(Job).offset(skip).limit(limit).all()

    def add(self, job: Job) -> Job:
        with self.session_factory() as session:
            session.add(job)
            session.commit()
            session.refresh(job)
            return job

