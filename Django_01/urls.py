from django.contrib import admin
from django.urls import path
from . import view


urlpatterns = [
    path('', view.home),
    path('count/', view.count),
    path('about/', view.about),
]
