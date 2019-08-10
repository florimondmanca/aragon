import typesystem as ts


class Rule(ts.Schema):
    id = ts.Integer()
    pattern = ts.String()
    is_regex = ts.Boolean()


class RuleCreate(ts.Schema):
    pattern = ts.String()
    is_regex = ts.Boolean(default=False)


ACTION_ADD = "add"
ACTION_REMOVE = "remove"
ACTIONS = {ACTION_ADD, ACTION_REMOVE}
