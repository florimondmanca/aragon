import typing

from faust.serializers.codecs import json


class nullable_json(json):
    def _dumps(self, value: typing.Any) -> typing.Optional[bytes]:  # type: ignore
        if value is None:
            return None
        return super()._dumps(value)
