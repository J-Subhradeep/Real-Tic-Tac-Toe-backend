from django.urls import path
from . import consumers
websocket_urlpatterns = [
    path('ws/seconduser/<str:grp_name>/<str:client_name>/',
         consumers.SecondUserConsumer.as_asgi()),
    path('ws/chat/<str:grp_name>/<str:sym>/',
         consumers.ChatConsumer.as_asgi()),
    path('ws/board/<str:grp_name>/',
         consumers.BoardConsumer.as_asgi()),
]
