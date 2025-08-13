from django.urls import path
from .views import *

urlpatterns = [
    path('chatgroup/<str:group_name>/', chat_group, name='chat_group'),
]