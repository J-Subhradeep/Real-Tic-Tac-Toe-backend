from django.urls import path
from . import consumers
websocket_urlpatterns = [
    path('ws/seconduser/<str:grp_name>/<str:client_name>/',
         consumers.SecondUserConsumer.as_asgi()),
]
