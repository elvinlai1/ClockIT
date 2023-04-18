from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

from django.contrib.auth.models import User
from timestamps.models import Timestamp

def login_view(request):
    # Your login view code here

    # Create a new timestamp object
    employee_id = request.user.id
    current_time = datetime.now()
    timestamp = Timestamp.objects.create(employee_id=employee_id, timestamp=current_time)

    return redirect('dashboard')