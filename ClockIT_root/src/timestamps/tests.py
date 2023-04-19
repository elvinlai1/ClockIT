from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from datetime import datetime
from .models import Timestamps
from employee.models import Department, Employee
from django.db.models.functions import ExtractYear, ExtractMonth, ExtractDay


class TimestampsTestCase(TestCase):

    def setUp(self):
        self.department = Department.objects.create(name='Engineering')
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )
        self.employee = Employee.objects.create(
            user=self.user,
            first_name='John',
            last_name='Doe',
            department=self.department
        )
    
    def test_filter_timestamps(self):
        self.client.login(username='testuser', password='testpass')
        # Make a POST request to create a new timestamp
        timestamp_data = {
            'employee': self.employee.id,
            'timestamp_in': timezone.now(),
        }
        response = self.client.post(reverse('timestamp_create'), data=timestamp_data)
        self.timestamp1 = Timestamps.objects.create(employee=self.employee, timestamp_in=datetime(2023, 4, 18, tzinfo=timezone.utc))
        queryset = Timestamps.objects.filter(timestamp_in__day=18)
        self.assertEqual(len(queryset), 2)
        self.assertEqual(queryset[0], self.timestamp1)

    
