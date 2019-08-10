import faust.app
from aiohttp.web import Application
from faust.web import Web

from aragon.core import settings

from .orm import create_schema, database
from .orm.middleware import model_error_middleware


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


app = App(
    "api",
    origin="aragon.api.app",
    autodiscover=["aragon.api.views"],
    broker=settings.KAFKA_BOOTSTRAP_SERVERS,
)
