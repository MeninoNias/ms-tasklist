import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker, Session
from task.core.database import Base as table_registry, get_session
from task.main import app


@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()

    table_registry.metadata.drop_all(engine)


@pytest.fixture
def client(session):
    def get_session_override():
        try:
            yield session
        finally:
            session.close()

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()
