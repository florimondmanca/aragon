from starlette.responses import JSONResponse
from starlette.routing import Route, Router


async def get_rules(request):
    return JSONResponse([])


async def create_rule(request):
    return JSONResponse({}, status_code=201)


async def remove_rule(request):
    return JSONResponse({}, status_code=204)


router = Router(
    routes=[
        Route("/", methods=["GET"], endpoint=get_rules),
        Route("/", methods=["POST"], endpoint=create_rule),
        Route("/{pk:int}", methods=["DELETE"], endpoint=remove_rule),
    ]
)
