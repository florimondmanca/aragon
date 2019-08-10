from starlette.config import Config
from databases import DatabaseURL
from starlette.datastructures import CommaSeparatedStrings

config = Config()

TESTING = False

DATABASE_URL = config("DATABASE_URL", cast=DatabaseURL)

KAFKA_RULES_TOPIC = config("KAFKA_RULES_TOPIC")
KAFKA_BOOTSTRAP_SERVERS = config("KAFKA_BOOTSTRAP_SERVERS", cast=CommaSeparatedStrings)
