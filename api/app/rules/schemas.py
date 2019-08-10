import typesystem as ts


class RuleCreate(ts.Schema):
    pattern = ts.String()
    is_regex = ts.Boolean(default=False)
