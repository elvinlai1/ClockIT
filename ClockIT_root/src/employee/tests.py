from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, timedelta
from .models import Employee, Department
from timestamps.models import Timestamps


# Create your tests here.
class EmployeeTestCase(TestCase):

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

    def test_timestamp_create(self):
        self.client.login(username='testuser', password='testpass')

        # Make a POST request to create a new timestamp
        timestamp_data = {
            'employee': self.employee.id,
            'timestamp_in': datetime.now(),
        }
        response = self.client.post(reverse('timestamp_create'), data=timestamp_data)

        # Check that the response was successful
        self.assertEqual(response.status_code, 302)

        # Check that a new Timestamps object was created with the correct data
        timestamp = Timestamps.objects.last()
        self.assertEqual(timestamp.employee, self.employee)
        #self.assertAlmostEqual(timestamp.timestamp_in, datetime.now(), delta=timedelta(seconds=1))
