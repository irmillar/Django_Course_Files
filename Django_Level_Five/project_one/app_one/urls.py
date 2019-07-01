from django.urls import path, include
from app_one import views

urlpatterns = [
    path('', views.basic, name='basic'),
]
