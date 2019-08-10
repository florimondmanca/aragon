from app import settings
from app.streaming import Producer

producer = Producer(settings.KAFKA_RULES_TOPIC)
