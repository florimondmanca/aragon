import typing


class ModelException(Exception):
    pass


class NoMatch(ModelException):
    def __init__(self, name: str, **kwargs: typing.Any):
        super().__init__()
        self.name = name
        self.kwargs = kwargs

    def __str__(self) -> str:
        query = ", ".join(f"{key}={value}" for key, value in self.kwargs.items())
        return f"{self.name} matching {query} does not exist".capitalize()
