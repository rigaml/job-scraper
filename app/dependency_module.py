from typing import Callable, ContextManager
from injector import Binder, Module, inject, provider, singleton
from sqlalchemy.orm import Session

import app.utils.file_utils as fu

from app import settings
from app.database.database import Database
from app.database.job_repository import JobRepositoryBase, JobRepository
from app.services.jobs_service import JobsServiceBase, JobsService

class DependencyModule(Module):
    def configure(self, binder: Binder):
        absolute_path_database = fu.get_absolute_path_in_parent(settings.JOBS_DATABASE_PATH_NAME)
        database_path= "sqlite:///" + absolute_path_database
        db = Database(database_path)

        binder.bind(Database, to=db, scope=singleton)        
        binder.bind(JobRepositoryBase, to=JobRepository, scope=singleton)
        binder.bind(JobsServiceBase, to=JobsService, scope=singleton)
