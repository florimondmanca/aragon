import faust.app
from aiohttp.web import Application
from faust.web import Request, Response, View, Web

from aragon.core import settings
from aragon.core.codecs import nullable_json
from aragon.core.models import RuleCreate

from .orm import create_schema, database
from .orm.middleware import model_error_middleware
from .orm.rules import Rule


class App(faust.app.App):
    class BootStrategy(faust.app.BootStrategy):
        enable_sensors = False

    producer_only = True

    def on_webserver_init(self, web: Web):
        _web: Application = web.web_app

        async def provide_db(_app: Application):
            if not database.is_connected:
                await database.connect()
                create_schema()

            yield

            if database.is_connected:
                await database.disconnect()

        _web.cleanup_ctx.append(provide_db)

        _web.middlewares.append(model_error_middleware)


app = App("api", broker=settings.KAFKA_BOOTSTRAP_SERVERS)

rules_topic = app.topic(
    settings.KAFKA_RULES_TOPIC, key_type=bytes, value_serializer=nullable_json()
)


@app.page("/rules")
class RulesList(View):
    async def get(self, request: Request) -> Response:
        return self.json(await Rule.get_all())

    async def post(self, request: Request) -> Response:
        data = dict(RuleCreate.validate(await request.json()))
        async with database.transaction():
            rule = await Rule.create(data=data)
            await app.send(
                rules_topic, key=str(rule["id"]), value={"action": "create", "data": rule}
            )
        return self.json(rule, status=201)


@app.page("/rules/{pk:\d+}")
class RulesDetail(View):
    async def get(self, request: Request, *, pk: int) -> Response:
        pk = int(pk)
        return self.json(await Rule.get(pk=pk))

    async def delete(self, request: Request, *, pk: int) -> Response:
        pk = int(pk)

        async with database.transaction():
            rule = await Rule.get(pk=pk)
            await Rule.destroy(pk=pk)

            await app.send(rules_topic, key=str(rule["id"]), value={"action": "delete"})
            # Send tombstone to eventually delete item from topic.
            await app.send(rules_topic, key=str(rule["id"]), value=None)

        return self.json({}, status=204)
