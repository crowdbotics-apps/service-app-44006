from django.urls import path, include
from .views import WebHookAPI
urlpatterns = [
    path("create-repos-webhook/", WebHookAPI.as_view())
]