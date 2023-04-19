from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from timestamps.models import Timestamps
from employee.models import Employee

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


def timestamp_edit(request, pk):
    timestamp = get_object_or_404(Timestamps, pk=pk)
    if request.method == 'POST':
        form = TimestampsForm(request.POST, instance=timestamp)
        if form.is_valid():
            timestamp = form.save()
            return redirect('timestamp_detail', pk=timestamp.pk)
    else:
        form = TimestampsForm(instance=timestamp)
    return render(request, 'timestamp_edit.html', {'form': form})

def test(request):
    return render(request, 'timestamp_test.html')