import json

import faust

from . import settings
from .datatypes import Rule

app = faust.App("rules-worker", broker=f"kafka://{settings.KAFKA_BROKER}")
rules = app.topic(settings.KAFKA_RULES_TOPIC, key_type=bytes, value_serializer="raw")


@app.agent(rules)
async def process_rules(stream: faust.streams.StreamT[Rule]):
    async for key, value in stream.items():
        if value is None:
            print(f"DELETE {key}")
        else:
            print(value)
            rule = Rule(**json.loads(value.decode("utf-8")))
            print(f"CREATE {key}: {rule}")
