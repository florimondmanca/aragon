import typing

from aiohttp.web import Request, Response, json_response, middleware

from .exceptions import NoMatch


@middleware
async def model_error_middleware(request: Request, handler: typing.Callable) -> Response:
    try:
        return await handler(request)
    except NoMatch as exc:
        return json_response({"error": str(exc)}, status=404)
