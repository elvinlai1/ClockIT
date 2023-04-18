from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

def dashboard(request):
    employee = Employee.objects.get(user=request.user)
    # TODO: Display employee's timestamps, work schedule, and other information
    context = {'employee': employee}
    return render(request, 'dashboard.html', context)

def employee_timestamps(request):
    employee = Employee.objects.get(user=request.user)
    timestamps = employee.timestamp_set.all()
    # TODO: Implement time window for editing timestamps
    context = {'timestamps': timestamps}
    return render(request, 'employee_timestamps.html', context)

def timeoff_request(request):
    # TODO: Implement time off request logic
    return HttpResponse('Submit a time off request')

def schedule(request):
    employee = Employee.objects.get(user=request.user)
    # TODO: Display employee's work schedule and allow shift change requests
    context = {'employee': employee}
    return render(request, 'schedule.html', context)

