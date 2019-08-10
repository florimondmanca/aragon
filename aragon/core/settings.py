from databases import DatabaseURL
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

config = Config()

TESTING = False

DATABASE_URL = config("DATABASE_URL", cast=DatabaseURL)

KAFKA_RULES_TOPIC = config("KAFKA_RULES_TOPIC")

KAFKA_BOOTSTRAP_SERVERS = config("KAFKA_BOOTSTRAP_SERVERS", cast=CommaSeparatedStrings)
assert len(KAFKA_BOOTSTRAP_SERVERS) > 0
