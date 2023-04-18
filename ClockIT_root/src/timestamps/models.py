from django.db import models
from django.contrib.auth.models import User

class Timestamps(models.Model):
    employee = models.ForeignKey('employee.Employee', on_delete=models.CASCADE)
    timestamp_in = models.DateTimeField()
    timestamp_out = models.DateTimeField(null=True, blank=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Timestamp for {self.employee} on {self.timestamp_in}'

class TimestampsLog(models.Model):
    timestamp = models.ForeignKey(Timestamps, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.updated_by} updated timestamp {self.timestamp} at {self.updated_at}'

