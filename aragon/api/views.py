from faust.web import Request, Response, View

from aragon.core import settings
from aragon.core.codecs import nullable_json
from aragon.core.models import RuleCreate

from .app import app
from .orm import database
from .orm.rules import Rule

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
