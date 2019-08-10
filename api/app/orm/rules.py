import typing

import sqlalchemy

from .db import database, metadata
from .exceptions import NoMatch

rules = sqlalchemy.Table(
    "rule",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("pattern", sqlalchemy.String(length=256)),
    sqlalchemy.Column("is_regex", sqlalchemy.Boolean),
)


class RuleManager:
    async def get_all(self) -> typing.List[dict]:
        query = rules.select()
        rows = await database.fetch_all(query)
        return [dict(row) for row in rows]

    async def get(self, pk: int) -> dict:
        row = await database.fetch_one(query=rules.select().where(rules.c.id == pk))
        if row is None:
            raise NoMatch("rule", pk=pk)
        return dict(row)

    async def create(self, data: dict) -> dict:
        pk = await database.execute(rules.insert(), values=data)
        return await self.get(pk=pk)

    async def destroy(self, pk: int) -> None:
        await database.fetch_all(rules.delete().where(rules.c.id == pk))


Rule = RuleManager()
