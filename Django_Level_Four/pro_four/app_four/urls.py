from django.urls import path
from . import views

# Allow Template Tagging by including the 'app_name' variable
app_name = 'app_four'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
