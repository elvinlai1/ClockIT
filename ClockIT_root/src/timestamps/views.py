from django.shortcuts import get_object_or_404, redirect, render
from myapp.models import Timestamps

def timestamps_edit(request, timestamp_id):
    timestamps = get_object_or_404(Timestamps, id=timestamps_id)
    employees = Employee.objects.all()
    departments = Department.objects.all()

    if request.method == 'POST':
        if 'action' in request.POST and request.POST['action'] == 'delete':
            timestamp.delete()
            return redirect('timestamps_list')
        else:
            timestamps.employee_id = request.POST['employee']
            timestamps.timestamps = request.POST['timestamp']
            timestamps.department_id = request.POST['department']
            timestamps.save()
            return redirect('timestamps_detail', timestamps_id=timestamps.id)

    return render(request, 'timestamps_edit.html', {
        'timestamps': timestamps,
        'employees': employees,
        'departments': departments,
    })

def timestamps_create(request):
    employees = Employee.objects.all()
    departments = Department.objects.all()

    if request.method == 'POST':
        timestamps = Timestamps()
        timestamps.employee_id = request.POST['employee']
        timestamps.timestamps = request.POST['timestamp']
        timestamps.department_id = request.POST['department']
        timestamps.save()
        return redirect('timestamps_detail', timestamps_id=timestamps.id)

    return render(request, 'timestamps_create.html', {
        'employees': employees,
        'departments': departments,
    })

def timestamps_list(request):
    timestamps = Timestamps.objects.all()
    return render(request, 'timestamps_list.html', {'timestamps': timestamps})

def timestamps_detail(request, timestamps_id):
    timestamps = get_object_or_404(Timestamps, id=timestamps_id)
    return render(request, 'timestamps_detail.html', {'timestamps': timestamps})

def timestamps_export(request):
    timestamps = Timestamps.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="timestamps.csv"'
    writer = csv.writer(response)
    writer.writerow(['Employee', 'Timestamps', 'Department'])
    for timestamps in timestamps:
        writer.writerow([timestamps.employee, timestamps.timestamps, timestamps.department])
    return response

def dashboard(request):
    employee = Employee.objects.get(user=request.user)

    context = {'employee': employee}
    return render(request, 'dashboard.html', context)

def employee_timestamps(request):
    employee = Employee.objects.get(user=request.user)
    timestamps = employee.timestamps_set.all()

    context = {'timestamps': timestamps}
    return render(request, 'employee_timestamps.html', context)

