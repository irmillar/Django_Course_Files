from django.urls import path
from app_five import views

urlpatterns = [
    path('', views.help_view, name="help"),
]
