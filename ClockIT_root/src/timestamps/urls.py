from django.urls import path
from . import views

urlpatterns = [
    path('', views.timestamp_create, name='timestamp_create'),
    path('edit/', views.timestamp_edit, name='timestamp_edit'),
    path('logout/', views.user_logout, name='logout'),
]