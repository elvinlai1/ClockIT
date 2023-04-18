from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('timestamps/', views.employee_timestamps, name='employee_timestamps'),
    path('timeoff/request/', views.timeoff_request, name='timeoff_request'),
    path('schedule/', views.schedule, name='schedule'),
    path('messages/', views.messages, name='messages'),
    path('news/', views.news, name='news'),
]
