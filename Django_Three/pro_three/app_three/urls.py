from django.urls import path
from app_three import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),
]
