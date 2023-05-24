from django.shortcuts import render, redirect
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic import FormView, CreateView

from .models import Employee, Department
from timestamps.models import Timestamps
from timestamps.utils import create_timestamp
from .forms import LoginForm, EmployeeSignUpForm, EmployeeProfileForm

# need disection of this class
# not generating session id
# class LoginView(FormView):
#     template_name = 'login.html'
#     form_class = LoginForm

#     def get_success_url(self):
#         print(self.request.user)
#         #create_timestamp(self.request)
#         user = self.request.user
#         if user.is_superuser:
#             # Redirect superusers to the admin site
#             return None
#         elif user.is_staff:
#             # Redirect staff members to the staff dashboard
#             return reverse_lazy('manager_dashboard') 
#         else:
#             # Redirect regular users to the user dashboard
#             return reverse_lazy('employee_dashboard')


def user_login(request):
    # needs to add check for isManager, isEmployee, isSuperuser tags
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # django authenticate function
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # check if user type and redirect to appropriate dashboard
            #
            #
            #
            # django login function
            login(request, user)
            # create timestamp
            create_timestamp(request) 
            return redirect('dashboard/')
        else:
            print("Error")
            prompt = {
                'order': 'Username or password is incorrect',
            }
            return render(request, 'login.html', prompt)
    else:
        return render(request, 'login.html')


def dashboard_employee(request):
    user = request.user
    employee = Employee.objects.get(user=user) 
    timestamps = Timestamps.objects.filter(employee=employee)

    context = {
        'employee': employee,
        'timestamps': timestamps
    }
    return render(request, 'dashboard_employee.html', context)

def dashboard_manager(request):
    user = request.user
    departments = Department.objects.all()
    employees = Employee.objects.all()
    today = timezone.now().date()
    
    context = {
        'employees': employees,
        'departments': departments,
    }

    return render(request, 'dashboard_manager.html', context)

def list_employees(request):
    employees = Employee.objects.all()
    departments = Department.objects.all()
    context = {
        'employees': employees,
        'departments':departments
    }
    return render(request, 'list_employees.html', context)

def profile_employee(request, pk):
    #get employee pk id from url
    #get employee object
    #get timestamps for employee
    employee = Employee.objects.get(pk=pk)
    employee_timestamps = Timestamps.objects.filter(employee=employee)

    context = {
        'employee': employee,
        'timestamps': employee_timestamps
    }
    return render(request, 'profile_employee.html', context)

def create_employee(request):
    form = EmployeeProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()
            return redirect('dashboard_manager')

    return render(request, 'create_employee.html', {'form': form})
    

