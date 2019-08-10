from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

config = Config()

TESTING = False

try:
    from databases import DatabaseURL

    DATABASE_URL = config("DATABASE_URL", cast=DatabaseURL)
except ImportError:
    DATABASE_URL = None

KAFKA_RULES_TOPIC = config("KAFKA_RULES_TOPIC")

KAFKA_BOOTSTRAP_SERVERS = config("KAFKA_BOOTSTRAP_SERVERS", cast=CommaSeparatedStrings)
assert len(KAFKA_BOOTSTRAP_SERVERS) > 0
