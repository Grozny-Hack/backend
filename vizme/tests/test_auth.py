import pytest
import pytest_asyncio
from blacksheep.testing import TestClient
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from vizme.app.auth.models import User
from vizme.auth.handlers import generate_tokens
from vizme.tests.factories.auth import UserFactory
from vizme.tests.utils import json_content, read_content


@pytest_asyncio.fixture
async def user():
    user = await UserFactory.create()
    return user


class TestLogin:
    @pytest.mark.asyncio
    async def test_success(self, user: User, client: TestClient):
        data = {"email": user.email, "password": "password"}
        response = await client.post("/api/auth/login", content=json_content(data))
        content = await read_content(response.content)
        assert content["code"] == 200

    @pytest.mark.asyncio
    async def test_wrong_password(self, user: User, client: TestClient):
        data = {"email": user.email, "password": "wrong_password"}
        response = await client.post("/api/auth/login", content=json_content(data))
        content = await read_content(response.content)
        assert content["code"] == 400

    @pytest.mark.asyncio
    async def test_wrong_email(self, user: User, client: TestClient):
        data = {"email": "wrong@email.com", "password": "password"}
        response = await client.post("/api/auth/login", content=json_content(data))
        content = await read_content(response.content)
        assert content["code"] == 400


@pytest.mark.asyncio
async def test_refresh_token(user: User, client: TestClient):
    payload = generate_tokens(
        sub=str(user.id),
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
    )
    data = {"accessToken": payload["access_token"], "refreshToken": payload["refresh_token"]}
    response = await client.post("/api/auth/refresh-token", content=json_content(data))
    content = await read_content(response.content)
    assert content["code"] == 200


@pytest.mark.asyncio
async def test_registration(session: AsyncSession, client: TestClient):
    user_count = (await session.execute(select(func.count(User.id)))).scalars().first()
    assert user_count == 0
    data = {
        "email": "string@string.com",
        "password": "string",
    }
    response = await client.post("/api/auth/registration", content=json_content(data))
    content = await read_content(response.content)
    assert content["code"] == 200
    user_count = (await session.execute(select(func.count(User.id)))).scalars().first()
    assert user_count == 1
