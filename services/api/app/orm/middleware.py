from starlette.responses import JSONResponse
from starlette.types import ASGIApp, Receive, Scope, Send

from .exceptions import NoMatch


class ModelExceptionMiddleware:
    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        try:
            await self.app(scope, receive, send)
        except NoMatch as exc:
            response = JSONResponse({"message": str(exc)}, status_code=404)
            await response(scope, receive, send)
