from starlette.applications import Starlette

from . import rules
from .orm import setup_db

app = Starlette()
setup_db(app)

app.router.mount("/rules", rules.router)
