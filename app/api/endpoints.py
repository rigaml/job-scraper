import logging
from typing import List
from fastapi import APIRouter
from app.api.job_response import JobResponse
from app.services.jobs_service import JobsServiceBase

logger = logging.getLogger(__name__)

class Endpoints:
    def __init__(self, jobs_service: JobsServiceBase):
        self.jobs_service = jobs_service
        self.router = APIRouter()

        self.router.add_api_route("/", self.health, methods=["GET"])

        self.router.add_api_route("/jobs/", self.get_jobs, methods=["GET"])

    def health(self):
        logger.debug("Accessing health")
        return {"health_check": "OK"}

    def get_jobs(self, skip: int = 0, limit: int = 10) -> List[JobResponse]:
        logger.debug("Accessing get_jobs")
        jobs = self.jobs_service.get_jobs(skip, limit)
        return [JobResponse.create_from_dto(job) for job in jobs]

