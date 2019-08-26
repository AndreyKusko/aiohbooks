import aiohttp_jinja2
import jinja2
from aiohttp import web
from aiohttp_session import (SimpleCookieStorage, get_session,
                             session_middleware, setup)

from main_files.routes import routes
from main_files.settings import BASE_DIR


app = web.Application()
for route in routes:
    app.router.add_route(route[0], route[1], route[2], name=route[3])


aiohttp_jinja2.setup(
    app,
    loader=jinja2.FileSystemLoader(str(BASE_DIR / 'main_files' / 'templates'))
)

setup(app, SimpleCookieStorage())

web.run_app(app)
