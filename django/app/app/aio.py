from aiohttp import web
from aiohttp_wsgi import WSGIHandler
from .wsgi import application


wsgi_handler = WSGIHandler(application)
aioapp = web.Application()
aioapp.router.add_route('*', '/{path_info:.*}', wsgi_handler)