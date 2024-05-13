from django.urls import path
from tokenapi.views import CustomAuthToken

urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view()),
]