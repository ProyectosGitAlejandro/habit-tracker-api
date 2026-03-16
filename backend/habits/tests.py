from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Habit


class HabitTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123"
        )

        self.client.login(username="testuser", password="testpassword123")

    def test_create_habit(self):
        """
        Test creating a new habit.
        """

        url = "/api/habits/"

        data = {
        "name": "Read 20 pages",
        "description": "Daily reading habit",
        "frequency": "daily"
    }

        response = self.client.post(url, data)
        print(response.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 1)