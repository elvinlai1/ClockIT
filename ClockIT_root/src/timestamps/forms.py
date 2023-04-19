from django import forms
from employee.models import Employee
from .models import Timestamps


class TimestampsForm(forms.ModelForm):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all())
    timestamp_in = forms.DateTimeField()
    timestamp_out = forms.DateTimeField(required=False)
    is_approved = forms.BooleanField(required=False)

    class Meta:
        model = Timestamps
        fields = ['employee', 'timestamp_in', 'timestamp_out', 'is_approved']