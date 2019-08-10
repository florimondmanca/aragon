import sqlalchemy
from databases import Database

from aragon.core import settings

database = Database(url=settings.DATABASE_URL, force_rollback=settings.TESTING)
metadata = sqlalchemy.MetaData()


def create_schema():
    engine = sqlalchemy.create_engine(str(database.url))
    metadata.create_all(engine)
