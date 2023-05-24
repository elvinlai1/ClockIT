from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('dashboard/', views.dashboard_employee, name='dashboard_employee'),
    path('manager-dashboard/', views.dashboard_manager, name='dashboard_manager'),
    path('profile/<int:pk>/', views.profile_employee, name='profile_employee'),
    path('list/', views.list_employees, name='list_employees'),
    path('create/', views.create_employee, name='create_employee'),
]
 