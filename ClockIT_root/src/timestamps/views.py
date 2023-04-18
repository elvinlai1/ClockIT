from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from timestamps.models import Timestamps
from employee.models import Employee

def timestamp_create(request):
    # Get the currently logged in user
    user = request.user

    # Get the employee associated with the user
    employee = Employee.objects.get(user=user)

    # Create a new Timestamps object with the current time as timestamp_in
    Timestamps.objects.create(employee=employee, timestamp_in=timezone.now())

    # Redirect to the homepage
    return redirect('/')


def timestamp_edit(request, pk):
    timestamp = get_object_or_404(Timestamps, pk=pk)
    if request.method == 'POST':
        form = TimestampsForm(request.POST, instance=timestamp)
        if form.is_valid():
            timestamp = form.save()
            return redirect('timestamp_detail', pk=timestamp.pk)
    else:
        form = TimestampsForm(instance=timestamp)
    return render(request, 'timestamps/timestamp_edit.html', {'form': form})


## employee login with GET request to create new timestamp

