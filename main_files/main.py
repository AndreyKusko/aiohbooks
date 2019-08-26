import aiohttp_jinja2
import jinja2
from aiohttp import web
from aiohttp_session import (SimpleCookieStorage, get_session,
                             session_middleware, setup)
from aiohttp_session.cookie_storage import EncryptedCookieStorage

# from routes import setup_routes
from routes import routes
from settings import BASE_DIR

# from middlewares import setup_middlewares

app = web.Application()
for route in routes:
    app.router.add_route(route[0], route[1], route[2], name=route[3])

# setup_middlewares(app)

# setup_routes(app)
# app['config'] = config

aiohttp_jinja2.setup(
    app,
    loader=jinja2.FileSystemLoader(str(BASE_DIR / 'main_files' / 'templates'))
)
# app.middlewares.append(middleware)
# app.middlewares.append(aiohttp_session.SimpleCookieStorage())
setup(app, SimpleCookieStorage())

web.run_app(app)
