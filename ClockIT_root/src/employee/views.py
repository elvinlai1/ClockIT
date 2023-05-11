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
from .forms import LoginForm, EmployeeSignUpForm

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

class EmployeeSignUpView(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('teachers:quiz_change_list')


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
            prompt = {
                'order': 'Username or password is incorrect',
            }
            return render(request, 'login.html', prompt)
    else:
        return render(request, 'login.html')


def employee_dashboard(request):
    user = request.user
    employee = Employee.objects.get(user=user) 
    timestamps = Timestamps.objects.filter(employee=employee)

    context = {
        'employee': employee,
        'timestamps': timestamps
    }
    return render(request, 'employee_dashboard.html', context)

def manager_dashboard(request):
    user = request.user
    departments = Department.objects.all()
    employees = Employee.objects.all()
    today = timezone.now().date()
    
    context = {
        'employees': employees,
        'departments': departments,
    }

    return render(request, 'manager_dashboard.html', context)
