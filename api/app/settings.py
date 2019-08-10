from starlette.config import Config
from databases import DatabaseURL

config = Config()

DATABASE_URL = config("DATABASE_URL", cast=DatabaseURL)
TESTING = False
