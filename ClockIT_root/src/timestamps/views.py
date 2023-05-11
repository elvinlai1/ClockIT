from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import logout
from django.utils import timezone
from django.forms import modelform_factory
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView
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
        form.save(commit=False)
        # duration column
        duration = timestamp.timestamp_out - timestamp.timestamp_in
        timestamp.duration = duration
        timestamp.save()
        return reverse_lazy('create_timestamp')
    else:
        form = TimestampForm()
    return render(request, 'create_timestamp.html', {'form': form})

def edit_timestamp(request, pk):
    timestamp = get_object_or_404(Timestamps, pk=pk)
    form = TimestampForm(request.POST or None, instance=timestamp)
    if form.is_valid():
        form.save()
        return redirect('timestamp_detail', pk=pk)
    else:
        # Render the form with the data from the timestamp instance
        form = TimestampForm(instance=timestamp)

    return render(request, 'edit_timestamp.html', {'form': form, 'timestamp': timestamp})

class TimestampDeleteView(DeleteView):
    model = Timestamps
    success_url = reverse_lazy('employee_dashboard')
    pk = 'timestamp_id'
    template_name = 'delete_timestamp.html'

    
