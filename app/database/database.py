"""
Databases base class.
"""

from contextlib import contextmanager
from typing import Generator
import logging

from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)

Base = declarative_base()


class Database:
    """Base class to help manage database connection and session creation for SQLAlchemy."""

    def __init__(self, db_url: str) -> None:
        """Initializes the database connection using the provided URL."""
        self._engine = create_engine(db_url)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )

    def create_database(self) -> None:
        """
        Creates all database tables.
        NOTE: In file where run this command, import all files that map the tables to be created.
        NOTE: Only need to run once, as once database is created don't need to execute again.
        """
        Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Generator[Session, None, None]:
        """Provides a context manager for creating database sessions."""
        session: Session = self._session_factory()
        try:
            yield session
        except Exception as e:
            logger.exception("Session rollback because of exception: %s", e)
            session.rollback()
            raise
        finally:
            session.close()
