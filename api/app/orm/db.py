import sqlalchemy
from starlette.applications import Starlette

from databases import Database

from app import settings

database = Database(url=settings.DATABASE_URL, force_rollback=settings.TESTING)
metadata = sqlalchemy.MetaData()


def setup_db(app: Starlette):
    @app.on_event("startup")
    async def _():
        engine = sqlalchemy.create_engine(str(database.url))
        metadata.create_all(engine)
        await database.connect()

    app.add_event_handler("shutdown", database.disconnect)
