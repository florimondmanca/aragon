from starlette.requests import Request
from starlette.responses import JSONResponse

from app.orm import database
from app.orm.rules import Rule

from .schemas import RuleCreate


async def get_all(request: Request):
    return JSONResponse(await Rule.get_all())


async def get(request: Request):
    return JSONResponse(await Rule.get(pk=request.path_params["pk"]))


async def create(request: Request):
    data = dict(RuleCreate.validate(await request.json()))
    async with database.transaction():
        rule = await Rule.create(data=data)
    return JSONResponse(rule, status_code=201)


async def remove(request: Request):
    pk = request.path_params["pk"]
    async with database.transaction():
        await Rule.destroy(pk=pk)
    return JSONResponse(status_code=204)
