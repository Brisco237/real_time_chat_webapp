from django.urls import path
from .views import *

urlpatterns = [
    path('chatgroup/<str:chat_group>/', chat_view, name='chat_group'),
]