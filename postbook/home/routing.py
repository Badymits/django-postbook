from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("ws/socket-server/<str:username>/", consumers.NotifConsumer.as_asgi()),
]

