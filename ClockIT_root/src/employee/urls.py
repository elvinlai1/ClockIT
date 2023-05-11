from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('manager-dashboard/', views.manager_dashboard, name='manager_dashboard'),
]
 