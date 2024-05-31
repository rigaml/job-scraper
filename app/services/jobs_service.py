from typing import List

from fastapi import Depends
from app.services.job_dto import JobDTO
from database.job_repository import JobRepository


class JobsService:

    def __init__(self, job_repository=Depends(JobRepository)):
        self._repository: JobRepository = job_repository

    def get_jobs(self, skip: int = 0, limit: int = 0) -> List[JobDTO]:
        jobs = self._repository.get_jobs(skip, limit)
        return [JobDTO.create_from_db(job) for job in jobs]
