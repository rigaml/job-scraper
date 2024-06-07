from fastapi import FastAPI

from app.api.endpoints import Endpoints
from app.services.jobs_service import JobsService

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True})

app.include_router(Endpoints(JobsService).router)

