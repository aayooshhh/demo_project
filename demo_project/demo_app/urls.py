from django.urls import path
from .views import FirstAPI

urlpatterns = [
    path('first/',FirstAPI.as_view())
]