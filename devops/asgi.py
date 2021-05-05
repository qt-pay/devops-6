"""
ASGI config for devops project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devops.settings')

application = get_asgi_application()


# # mysite/asgi.py
# import os
#
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application
# import hisconsole.routing
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devops.settings")
#
# application = ProtocolTypeRouter({
#   "http": get_asgi_application(),
#   "websocket": AuthMiddlewareStack(
#         URLRouter(
#             hisconsole.routing.websocket_urlpatterns
#         )
#     ),
# })