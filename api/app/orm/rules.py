import sqlalchemy

from .db import metadata

rules = sqlalchemy.Table(
    "rule",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("pattern", sqlalchemy.String(length=256)),
    sqlalchemy.Column("is_regex", sqlalchemy.Boolean),
)
