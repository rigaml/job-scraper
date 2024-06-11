import json
import logging
import logging.config

from typing import List

from fastapi import FastAPI
from injector import Injector

from app.dependency_module import DependencyModule
from app.services.jobs_service import JobsServiceBase
from app.api.job_response import JobResponse

def init_logger():
    """
    Initialize and return the module logger.
    """
    return logging.getLogger(__name__)


def load_logging_config(config_path="app/logging_config.json"):
    """
    Load logging configuration from a JSON file.
    """
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
        logging.config.dictConfig(config)
        
load_logging_config() 
logger = init_logger()

app = FastAPI(title="Scrape Jobs API", swagger_ui_parameters={"tryItOutEnabled": True})

injector = Injector([DependencyModule()])

@app.get("/")
def health():
    return {"health_check": "OK"}

@app.get("/jobs/", response_model=List[JobResponse])
def get_jobs(skip: int = 0, limit: int = 10)-> List[JobResponse]:
    jobs_service= injector.get(JobsServiceBase)
    jobs = jobs_service.get_jobs(skip, limit)
    response= [JobResponse.create_from_dto(job) for job in jobs]
    return response




