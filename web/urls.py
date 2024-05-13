from django.urls import path
from tokenapi.views import CustomAuthToken
from .views import index

urlpatterns = [
    path("", index),
]