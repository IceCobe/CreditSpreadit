from django.urls import path
from django.http import HttpResponse

from .views import hello_world

urlpatterns = [
    path('', hello_world),
]
