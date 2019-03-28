"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from aiohttp import web
from aiohttp_wsgi import WSGIHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_wsgi_application()


wsgi_handler = WSGIHandler(application)
aioapp = web.Application()
aioapp.router.add_route('*', '/{path_info:.*}', wsgi_handler)