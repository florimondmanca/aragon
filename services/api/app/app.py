from starlette.applications import Starlette

from . import rules
from .orm import database, create_schema
from .orm.middleware import ModelExceptionMiddleware

app = Starlette()


@app.on_event("startup")
async def setup_db():
    create_schema()
    await database.connect()


app.add_event_handler("shutdown", database.disconnect)
app.add_middleware(ModelExceptionMiddleware)

app.add_event_handler("startup", rules.producer.connect)
app.add_event_handler("shutdown", rules.producer.disconnect)

app.mount("/rules", rules.router)
