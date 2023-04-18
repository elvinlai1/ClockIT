from django.urls import path
from . import views

urlpatterns = [
    path('', views.timestamp_list, name='timestamp_list'),
    path('new/', views.timestamp_create, name='timestamp_create'),
    path('edit/<int:pk>/', views.timestamp_edit, name='timestamp_edit'),
    path('export/', views.timestamp_export, name='timestamp_export'),
]