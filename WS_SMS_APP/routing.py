from django.urls import path
from . import consumers
websocket_urlpatterns =[
    path('ws/room/<str:code>/',consumers.ConnectionSMSWebSocket.as_asgi())
]