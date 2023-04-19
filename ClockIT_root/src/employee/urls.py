from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('timestamps/', views.employee_timestamps, name='employee_timestamps'),
    path('login/', views.user_login, name='login'),

]
