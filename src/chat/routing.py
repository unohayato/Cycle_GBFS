from django.urls import re_path

from chat import comsumers

websocket_urlpatterns = [
  re_path("ws/chat/(?P<room_name>\w+)/$", comsumers.ChatConsumer.as_asgi()),
]