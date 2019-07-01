from django.urls import path
from pfour_app import views

urlpatterns = [
    path('', views.index, name='index'),
]
