import pytest
from fastapi.testclient import TestClient

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from task.core.database import get_db
from task.models import Base as table_registry
from task.main import app

SQLALCHEMY_DATABASE_URL_TEST = 'sqlite:///:memory:'
engine = create_engine(SQLALCHEMY_DATABASE_URL_TEST, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def client(session):
    def get_session_override():
        return session

    app.dependency_overrides[get_db] = get_session_override
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()


@pytest.fixture(scope="module")
def session():
    table_registry.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        table_registry.metadata.drop_all(bind=engine)
