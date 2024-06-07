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
        job1 = JobDTO(
            ref="ref1",
            title="title1",
            salary="salary1",
            loc="loc1",
            job_type="type1",
            skills="skills1",
            duration="duration1",
            start_date="start_date1",
            rate="rate1",
            recruiter="recruiter1",
            posted_date="posted_date1",
            permalink="permalink1"
        )
        job2 = JobDTO(
            ref="ref2",
            title="title2",
            salary="salary2",
            loc="loc2",
            job_type="type2",
            skills="skills2",
            duration="duration2",
            start_date="start_date2",
            rate="rate2",
            recruiter="recruiter2",
            posted_date="posted_date2",
            permalink="permalink2"
        )

        return [job1, job2]

        # jobs = self._repository.get_jobs(skip, limit)
        # return [JobDTO.create_from_db(job) for job in jobs]
