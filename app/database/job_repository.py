"""
Jobs repository
"""

from abc import ABC, abstractmethod
from typing import List, Optional
from injector import inject
from sqlalchemy import and_

from app.database.database import Database
from app.database.job import Job

class JobRepositoryBase(ABC):

    @abstractmethod
    def get_by_hash_key(self, jobs_site_id: int, hash_key: str) -> Optional[Job]:
        pass

    @abstractmethod
    def get_jobs(self, skip: int = 0, limit: int = 0) -> List[Job]:
        pass

    @abstractmethod
    def add(self, job: Job) -> Job:
        pass

class JobRepository:

    @inject
    def __init__(self, database: Database):
        self.session_factory = database.session

    def get_by_hash_key(self, jobs_site_id: int, hash_key: str) -> Optional[Job]:
        with self.session_factory() as session:
            return session.query(Job).filter(and_(Job.jobs_site_id == jobs_site_id, Job.hash_key == hash_key)).one_or_none()

    def get_jobs(self, skip: int = 0, limit: int = 10) -> List[Job]:
        with self.session_factory() as session:
            return session.query(Job).offset(skip).limit(limit).all()

    def add(self, job: Job) -> Job:
        with self.session_factory() as session:
            session.add(job)
            session.commit()
            session.refresh(job)
            return job

