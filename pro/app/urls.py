from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('mounika/',views.mounika),
    path('home/',views.home),
    path('singledata/'views.singledata)
]