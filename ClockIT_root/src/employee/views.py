from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Employee
from timestamps.utils import create_timestamp


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            create_timestamp(request)
            return redirect(reverse('dashboard'))
        else:
            
            return HttpResponse('Invalid login')

    else:
       
        return render(request, 'login.html')



def dashboard(request):
    # Your dashboard view code here
    return render(request, 'dashboard.html')

def employee_timestamps(request):
    # Your employee_timestamps view code here
    return render(request, 'employee_timestamps.html')


def test_page(request):
    return render(request, 'employee_test.html')