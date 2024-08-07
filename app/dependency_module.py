from injector import Binder, Module, singleton

from app import config
from app.database.database import Database
from app.database.job_repository import JobRepositoryBase, JobRepository
from app.services.jobs_service import JobsServiceBase, JobsService

class DependencyModule(Module):
    def configure(self, binder: Binder):
        database_uri= "sqlite:///" + config.JOBS_DATABASE_PATH_NAME
        db = Database(database_uri)

        binder.bind(Database, to=db, scope=singleton)
        binder.bind(JobRepositoryBase, to=JobRepository, scope=singleton)
        binder.bind(JobsServiceBase, to=JobsService, scope=singleton)
