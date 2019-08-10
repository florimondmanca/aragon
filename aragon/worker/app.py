import faust.app

from aragon.core import settings
from aragon.core.models import Rule, ACTIONS, ACTION_ADD, ACTION_REMOVE


class App(faust.app.App):
    class BootStrategy(faust.app.BootStrategy):
        enable_sensors = False


app = App("worker", broker=settings.KAFKA_BOOTSTRAP_SERVERS)

rules_topic = app.topic(settings.KAFKA_RULES_TOPIC, key_type=bytes, value_serializer="json")


@app.agent(rules_topic)
async def process_rules(stream: faust.streams.StreamT[Rule]):
    async for key, event in stream.items():
        action: str = event["action"]
        if action not in ACTIONS:
            print(f"UNKNOWN ACTION: {action}")
            continue

        if action == ACTION_ADD:
            rule = Rule(**event["data"])
            print(f"ADD @{key}: {rule}")

        elif action == ACTION_REMOVE:
            print(f"REMOVE @{key}")
