from django import forms
from .models import Timestamps
from django.forms.widgets import DateTimeInput

class TimestampForm(forms.ModelForm):
    class Meta:
        model = Timestamps
        fields = ['employee', 'timestamp_in', 'timestamp_out']
        widgets = {
            'timestamp_in': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'timestamp_out': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }