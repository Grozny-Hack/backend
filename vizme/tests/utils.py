from typing import Any

from blacksheep import Content
from essentials.json import dumps
from orjson import loads
from sqlalchemy.orm import scoped_session

from vizme.db.base import test_session_maker


def json_content(data: Any) -> Content:
    return Content(
        b"application/json",
        dumps(data, separators=(",", ":")).encode("utf8"),
    )


async def read_content(content: Content | None):
    if not content:
        raise AssertionError("Content is None")
    data = await content.read()
    if data == b"Resource not found":
        raise AssertionError("Resource not found")
    return loads(data.decode())


sc_session = scoped_session(test_session_maker)
