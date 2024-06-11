from abc import ABC, abstractmethod
from typing import List

from injector import inject

from app.services.job_dto import JobDTO
from app.database.job_repository import JobRepositoryBase


class JobsServiceBase(ABC):
    @abstractmethod
    def get_jobs(self, skip: int = 0, limit: int = 0) -> List[JobDTO]:
        pass

class JobsService(JobsServiceBase):

    @inject
    def __init__(self, job_repository: JobRepositoryBase):
        self._repository = job_repository

    def get_jobs(self, skip: int = 0, limit: int = 0) -> List[JobDTO]:
        jobs = self._repository.get_jobs(skip, limit)
        return [JobDTO.create_from_db(job) for job in jobs]
