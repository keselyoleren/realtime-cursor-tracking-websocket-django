from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from django.urls import path
import os
from cursor.consumers import cursor

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telelab.settings')

application = ProtocolTypeRouter({
    'websocket': 
        URLRouter([
                path('ws/stream/', cursor)
            ]
        )
})