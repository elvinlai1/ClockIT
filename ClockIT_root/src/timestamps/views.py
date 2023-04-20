from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import logout
from django.utils import timezone
from django.forms import modelform_factory
from timestamps.models import Timestamps
from employee.models import Employee, Department
from django.urls import reverse
from .forms import TimestampsForm

def user_logout(request):
    logout(request)
    return redirect('login')

def timestamp_create(request):
    user = request.user
    employee = Employee.objects.get(user=user)
    today = timezone.now().date()

    # Compare the current date with the timestamp_in date
    if Timestamps.objects.filter(employee=employee, timestamp_in__date=today).exists():
        # If the employee already has a timestamp_in, add a timestamp_out
        timestamp = Timestamps.objects.get(employee=employee, timestamp_in__date=today)
        timestamp.timestamp_out = timezone.now()
        timestamp.save()
    else:
        # If the employee doesn't have a timestamp_in, create a new timestamp_in
        Timestamps.objects.create(employee=employee, timestamp_in=timezone.now())
            
    return redirect('/')

def timestamp_edit(request):
    # Get timestamps
    # Edit timestamp
    # Delete timestamp
    # Create timestamp

    employees = Employee.objects.all()
    timestamps = None
    selected_employee = None

    # if request.method == 'GET':
    #     employees = Employees.objects.all()
    #     context = {'employees': employees}
    
    # if request.method == 'GET':
    #     selected_employee_id = request.GET.get('employee')
    #     selected_employee = Employee.objects.get(id=selected_employee_id)
    #     timestamps = Timestamps.objects.filter(employee=selected_employee)


    # if request.method == 'POST':
    #     # save the form data to the database
    #     selected_employee_id = request.POST.get('employee')
    #     selected_employee = Employee.objects.get(id=selected_employee_id)
    #     timestamps = Timestamps.objects.filter(employee=selected_employee)
    form = TimestampsForm(request.POST or None)

    

    context = {
        'employees': employees,
        'timestamps': timestamps,
        'selected_employee': selected_employee,
        'form': form,
    }

    return render(request, 'timestamp_edit.html', context)