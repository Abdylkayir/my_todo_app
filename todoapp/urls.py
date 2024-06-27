from django.urls import path
from todoapp.views import home

urlpatterns = [
    path('', home),
]
