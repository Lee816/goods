"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

from chat.consumers import ChatComsumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter(
                    [
                        path("ws/<int:pk>/chatroom", ChatComsumer.as_asgi()),
                    ]
                )
            )
        ),
    }
)
