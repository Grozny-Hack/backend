from typing import Awaitable, Callable

from blacksheep import Application, Request, Response, json
from blacksheep.server.authorization import Policy
from guardpost import UnauthorizedError
from guardpost.common import AuthenticatedRequirement

from vizme import exceptions
from vizme.app.auth.controllers import AuthorizationController
from vizme.auth.handlers import AuthHandler
from vizme.docs import docs
from vizme.logger import logger
from vizme.protocol import Response as MyResponse

app = Application()

app.register_controllers([AuthorizationController])

docs.bind_app(app)


class ExampleMiddleware:
    async def __call__(self, request: Request, handler: Callable[[Request], Awaitable[Response]]) -> Response:
        # TODO LOgs
        response = await handler(request)
        if request.path == "/api/google-callback":
            response.remove_header(b"Location")
            response.set_header(b"Location", b"/api/google")
        return response


app.use_cors(
    allow_methods="*",
    allow_origins="*",
    allow_headers="* Authorization",
    max_age=300,
)
app.middlewares.append(ExampleMiddleware())


app.use_authentication().add(AuthHandler())
app.use_authorization().add(Policy("user", AuthenticatedRequirement()))


@app.exception_handler(Exception)
async def uvicorn_base_exception_handler(self, request: Request, exc: Exception):
    logger.debug(exc)
    error = exceptions.ServerError(message=str(exc))
    return json(
        MyResponse(
            code=error.status_code,
            message=error.message,
            exception_class="ServerError",
        ).dict()
    )


@app.exception_handler(exceptions.ApiException)
async def unicorn_api_exception_handler(self, request: Request, exc: exceptions.ApiException):
    logger.debug(exc.message)

    return json(MyResponse(code=exc.status_code, message=exc.message, exception_class=exc._type()).dict())


@app.exception_handler(UnauthorizedError)
async def guardpost_api_exception_handler(self, request: Request, exc: UnauthorizedError):
    logger.debug(exc)
    error = exceptions.UnauthorizedError()
    return json(
        MyResponse(
            code=error.status_code,
            message=error.message,
            exception_class=error._type(),
        ).dict()
    )


@app.exception_handler(400)
async def validation_exception_handler(self, request: Request, exc):
    logger.debug(exc)
    error = exceptions.ValidationError(message=str(exc))
    return json(
        MyResponse(
            code=error.status_code,
            message=error.message,
            exception_class=error._type(),
        ).dict()
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=5000)
