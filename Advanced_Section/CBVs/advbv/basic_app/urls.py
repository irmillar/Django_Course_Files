from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    # path('detail/', views.SchoolDetailView.as_view(), name='detail'),
]
