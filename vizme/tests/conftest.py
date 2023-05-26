from asyncio import get_event_loop_policy

import pytest
import pytest_asyncio
from blacksheep.testing import TestClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from main import app
from vizme.db import Base, TestSessionMaker, container, test_engine, test_session_maker


@pytest.fixture(scope="session")
def event_loop():
    policy = get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def prepare_db():
    # Clears previous tables in db and creates new ones
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()
        yield


@pytest_asyncio.fixture
async def session(prepare_db) -> AsyncSession:  # TODO: typing for fixture
    async with test_session_maker() as session:
        yield session


@pytest_asyncio.fixture
async def client() -> TestClient:  # TODO: typing for fixture
    await app.start()
    container.register(sessionmaker, TestSessionMaker)
    yield TestClient(app=app)
