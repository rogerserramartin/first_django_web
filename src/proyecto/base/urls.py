# we import the views here
from django.urls import path
# from this directory, import views.py
from . import views

urlpatterns = [path('', views.list_todo, name='pending')]  # base route, views.list_todo
