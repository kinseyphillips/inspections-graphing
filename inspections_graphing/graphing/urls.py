from django.urls import path
from . import views

urlpatterns = [
    path('', views.chart, name='pie_graph'),
]