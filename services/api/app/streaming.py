import asyncio
import json
import typing

from aiokafka import AIOKafkaProducer

from . import settings


class Producer:
    _producer: AIOKafkaProducer

    def __init__(self, topic: str, bootstrap_servers: str = None):
        if bootstrap_servers is None:
            bootstrap_servers = settings.KAFKA_BOOTSTRAP_SERVERS
        self.topic = topic
        self.bootstrap_servers = bootstrap_servers

    async def connect(self):
        loop = asyncio.get_event_loop()
        self._producer = AIOKafkaProducer(
            loop=loop,
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=lambda value: (
                json.dumps(value).encode("utf-8") if value is not None else None
            ),
            key_serializer=lambda key: str(key).encode("utf-8"),
        )
        # Get cluster layout and initial topic/partition leadership information
        await self._producer.start()

    async def send(self, event: typing.Optional[dict], key: typing.Any):
        await self._producer.send_and_wait(self.topic, event, key=key)

    async def disconnect(self, *args):
        # Wait for all pending messages to be delivered or expire.
        await self._producer.stop()
