import sqlalchemy
from databases import Database
from starlette.applications import Starlette

from app import settings

from .middleware import ModelExceptionMiddleware

database = Database(url=settings.DATABASE_URL, force_rollback=settings.TESTING)
metadata = sqlalchemy.MetaData()


def setup_db(app: Starlette):
    @app.on_event("startup")
    async def _():
        engine = sqlalchemy.create_engine(str(database.url))
        metadata.create_all(engine)
        await database.connect()

    app.add_event_handler("shutdown", database.disconnect)
    app.add_middleware(ModelExceptionMiddleware)
