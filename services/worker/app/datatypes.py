from faust.models import Record


class Rule(Record, serializer="json"):
    id: int
    pattern: str
    is_regex: bool
