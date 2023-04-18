from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, timedelta

from .models import TimeStamps
from .views import index, TimeStamps_edit, TimeStamps_new

class TimeStampsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create_user('testuser', password='12345')
        TimeStamps.objects.create(employee=user, TimeStamps=datetime.now())

    def test_employee_label(self):
        TimeStamps = TimeStamps.objects.get(id=1)
        field_label = TimeStamps._meta.get_field('employee').verbose_name
        self.assertEqual(field_label, 'employee')

    def test_TimeStamps_label(self):
        TimeStamps = TimeStamps.objects.get(id=1)
        field_label = TimeStamps._meta.get_field('TimeStamps').verbose_name
        self.assertEqual(field_label, 'TimeStamps')

    def test_TimeStamps_str(self):
        TimeStamps = TimeStamps.objects.get(id=1)
        expected_str = f"{TimeStamps.employee.username} at {TimeStamps.TimeStamps.strftime('%m/%d/%Y %I:%M %p')}"
        self.assertEqual(str(TimeStamps), expected_str)

class TimeStampsViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.user = User.objects.create_user('testuser', password='12345')
        cls.TimeStamps = TimeStamps.objects.create(employee=cls.user, TimeStamps=datetime.now())

    def test_index_view_url_exists_at_desired_location(self):
        response = self.client.get('/TimeStampss/')
        self.assertEqual(response.status_code, 200)

    def test_index_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'TimeStamps/index.html')

    def test_TimeStamps_edit_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/TimeStampss/edit/{self.TimeStamps.id}/')
        self.assertEqual(response.status_code, 200)

    def test_TimeStamps_edit_view_url_accessible_by_name(self):
        response = self.client.get(reverse('TimeStampss_edit', args=[self.TimeStamps.id]))
        self.assertEqual(response.status_code, 200)

    def test_TimeStamps_edit_view_uses_correct_template(self):
        response = self.client.get(reverse('TimeStamps_edit', args=[self.TimeStamps.id]))
        self.assertTemplateUsed(response, 'TimeStamps/TimeStamps_edit.html')

    def test_TimeStamps_edit_view_post_edit(self):
        # Simulate form submission
        new_TimeStamps = datetime.now() - timedelta(hours=1)
        response = self.client.post(reverse('TimeStamps_edit', args=[self.TimeStamps.id]), {'TimeStamps': new_TimeStamps})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

        # Check that the TimeStamps was edited in the database
        updated_TimeStamps = TimeStamps.objects.get(id=self.TimeStamps.id)
        self.assertEqual(updated_TimeStamps.TimeStamps, new_TimeStamps)

    def test_TimeStamps_edit_view_post_delete(self):
        response = self.client.post(reverse('TimeStamps_edit', args=[self.TimeStamps.id]), {'delete': 'yes'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

        # Check that the TimeStamps was deleted from the database
        with self.assertRaises(TimeStamps.DoesNotExist):
            TimeStamps.objects.get(id=self.TimeStamps.id)

    def test_TimeStamps_edit_view_url_exists_at_desired_location(self):
        response = self.client.get('/TimeStamps/1/edit/')
        self.assertEqual(response.status_code, 200)

    def test_TimeStamps_edit_view_uses_correct_template(self):
        response = self.client.get(reverse('TimeStamps:edit', kwargs={'pk': 1}))
        self.assertTemplateUsed(response, 'TimeStamps/edit.html')
