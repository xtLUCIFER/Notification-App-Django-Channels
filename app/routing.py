from django.urls import re_path
from .consumers import TestConsumer

websocket_urlpatterns = [
    re_path(r'ws/notification/$', TestConsumer.as_asgi()),
]