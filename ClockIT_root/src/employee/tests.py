from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, timedelta
from django.utils import timezone
from .models import Employee, Department
from timestamps.models import Timestamps
from timestamps.utils import create_timestamp
from django.test import RequestFactory


# Create your tests here.
class EmployeeTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
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

    def test_user_login(self):
        response = self.client.post('/login/', {'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/dashboard/')
        # Check that a new timestamp was created
        today = timezone.now().date()
        timestamp = Timestamps.objects.get(employee__user__username='testuser', timestamp_in__date=today)
        self.assertIsNotNone(timestamp)


    def test_create_timestamp(self):
        # Make sure there are no existing timestamps for today
        today = timezone.now().date()
        self.client.login(username='testuser', password='testpass')
        request = self.factory.get('/')
        request.user = self.user

        # Call the create_timestamp view function
        response = create_timestamp(request)

        # Check that a timestamp was created for today
        self.assertEqual(Timestamps.objects.filter(employee=self.employee, timestamp_in__date=today).count(), 1)
        
        # Check that the timestamp has a timestamp_in value that is close to the current time
        timestamp = Timestamps.objects.get(employee=self.employee, timestamp_in__date=today)
        self.assertAlmostEqual(timestamp.timestamp_in, timezone.now(), delta=timezone.timedelta(seconds=1))
        
        # Check that the response is a redirect
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('dashboard'))


