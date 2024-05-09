from django.urls import path
from . import views

urlpatterns = [
    path('', views.pie_graph, name='pie_graph'),
]