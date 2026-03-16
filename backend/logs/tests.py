from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from habits.models import Habit
from .models import HabitLog


class HabitLogTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123"
        )

        self.client.login(username="testuser", password="testpassword123")

        self.habit = Habit.objects.create(
            user=self.user,
            name="Exercise",
            description="Daily workout"
        )

    def test_create_log(self):
        """
        Test creating a habit log.
        """

        url = "/api/logs/"

        data = {
            "habit": self.habit.id,
            "completed": True,
            "date": "2026-03-16"
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(HabitLog.objects.count(), 1)