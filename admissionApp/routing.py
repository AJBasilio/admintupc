from django.urls import re_path
from . import consumers


websocket_urlpatterns = [
    re_path(r'tupadmin/message/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'applicant/message/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'interviewer/message/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'nurse/message/$', consumers.ChatConsumer.as_asgi()),
]