from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import logout
from django.utils import timezone
from django.forms import modelform_factory
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView
from datetime import timedelta
from timestamps.models import Timestamps
from employee.models import Employee, Department
from .forms import TimestampForm

def user_logout(request):
    # reduce to single logout function
    logout(request)
    return redirect('login')



def create_timestamp(request):
    form = TimestampForm(request.POST or None)
    if form.is_valid():
        timestamp = form.save(commit=False)
        # Calculate duration
        duration = timestamp.timestamp_out - timestamp.timestamp_in
        timestamp.duration = duration
        timestamp.save()
        return redirect('create_timestamp')  # Use redirect instead of reverse_lazy

    return render(request, 'create_timestamp.html', {'form': form})


def edit_timestamp(request, pk):
    timestamp = get_object_or_404(Timestamps, pk=pk)
    form = TimestampForm(request.POST or None, instance=timestamp)
    if form.is_valid():
        form.save()
        return redirect('timestamp_detail', pk=pk)
    else:
        # Render the form with the data from the timestamp instanceG
        form = TimestampForm(instance=timestamp)

    return render(request, 'edit_timestamp.html', {'form': form, 'timestamp': timestamp})

def list_timestamps(request):
    timestamps = Timestamps.objects.all()
    employees = Employee.objects.all()

    context = {
        'timestamps': timestamps,
        'employees': employees,
    }

    return render(request, 'list_timestamps.html', context)

class TimestampDeleteView(DeleteView):
    model = Timestamps
    success_url = reverse_lazy('employee_dashboard')
    pk = 'timestamp_id'
    template_name = 'delete_timestamp.html'

    
