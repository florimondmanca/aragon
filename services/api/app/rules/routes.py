from starlette.routing import Route, Router

from . import views


router = Router(
    routes=[
        Route("/", methods=["GET"], endpoint=views.get_all),
        Route("/{pk:int}", methods=["GET"], endpoint=views.get),
        Route("/", methods=["POST"], endpoint=views.create),
        Route("/{pk:int}", methods=["DELETE"], endpoint=views.remove),
    ]
)
