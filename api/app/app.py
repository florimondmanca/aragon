from starlette.applications import Starlette

from .routers import rules

app = Starlette()
app.mount("/rules", rules.router)
