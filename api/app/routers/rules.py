from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route, Router

from app.orm import database
from app.orm.rules import rules


async def get_rules(request: Request):
    query = rules.select()
    rows = await database.fetch_all(query)
    print(rows)
    return JSONResponse([])


async def create_rule(request: Request):
    return JSONResponse({}, status_code=201)


async def remove_rule(request: Request):
    return JSONResponse({}, status_code=204)


router = Router(
    routes=[
        Route("/", methods=["GET"], endpoint=get_rules),
        Route("/", methods=["POST"], endpoint=create_rule),
        Route("/{pk:int}", methods=["DELETE"], endpoint=remove_rule),
    ]
)
