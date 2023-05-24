from django.urls import path
from . import views
from timestamps.views import TimestampDeleteView

urlpatterns = [
    path('list/', views.list_timestamps, name='list_timestamps'),
    path('create/', views.create_timestamp, name='create_timestamp'),
    path('edit/<int:pk>/', views.edit_timestamp, name='edit_timestamp'),
    path('delete/<int:pk>/', TimestampDeleteView.as_view(), name='delete_timestamp'),
    path('logout/', views.user_logout, name='logout'),
]