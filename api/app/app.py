from starlette.applications import Starlette

from .orm import database, setup_db
from .routers import rules

app = Starlette()
setup_db(app)

app.mount("/rules", rules.router)
