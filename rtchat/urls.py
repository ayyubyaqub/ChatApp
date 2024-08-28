
from rtchat.views import *
from django.urls import path, include

urlpatterns = [

    path('', chat_view, name="home"),
]
