from . import consumers
from django.urls import path

websocket_urlpatterns = [
    path('ws/<slug:room_slug>/', consumers.ChatConsumer.as_asgi()),
]