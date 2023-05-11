from django.utils import timezone
from timestamps.models import Timestamps
from employee.models import Employee
from django.shortcuts import redirect, reverse

def create_timestamp(request):
        user = request.user
        employee = Employee.objects.get(user=user)
        today = timezone.now().date()

        # Compare the current date with the timestamp_in date
        if Timestamps.objects.filter(employee=employee, timestamp_in__date=today).exists():
            # If the employee already has a timestamp_in, add a timestamp_out
            timestamp = Timestamps.objects.get(employee=employee, timestamp_in__date=today)
            timestamp.timestamp_out = timezone.now()
            timestamp.duration = timestamp.timestamp_out - timestamp.timestamp_in
            print('Timestamp out created')
            timestamp.save()
        else:
            # If the employee doesn't have a timestamp_in, create a new timestamp_in
            Timestamps.objects.create(employee=employee, timestamp_in=timezone.now())
            print('Timestamp in created')
                

