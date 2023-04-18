from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name