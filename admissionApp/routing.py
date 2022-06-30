from django.urls import re_path
from . import consumers


websocket_urlpatterns = [
    re_path('tupadmin/message/', consumers.ChatConsumer.as_asgi()),
    re_path('applicant/message/', consumers.ChatConsumer.as_asgi()),
    re_path('interviewer/message/', consumers.ChatConsumer.as_asgi()),
    re_path('nurse/message/', consumers.ChatConsumer.as_asgi()),
]