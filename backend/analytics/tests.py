from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from habits.models import Habit
from logs.models import HabitLog
from datetime import date


class AnalyticsTests(APITestCase):
    """
    Test suite for analytics endpoints.

    These tests ensure that user analytics and heatmap
    endpoints return correct responses and require authentication.
    """

    def setUp(self):
        """
        Create a test user and authenticate requests.
        """
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123"
        )

        self.client.force_authenticate(user=self.user)

        # Create test habit
        self.habit = Habit.objects.create(
            user=self.user,
            name="Read",
            frequency="daily"
        )

        # Create habit log
        HabitLog.objects.create(
            user=self.user,
            habit=self.habit,
            date=date.today(),
            completed=True
        )

    def test_get_analytics(self):
        """
        Test retrieving user analytics data.
        """
        response = self.client.get("/api/analytics/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("total_habits", response.data)
        self.assertIn("completed_today", response.data)
        self.assertIn("completion_rate", response.data)
        self.assertIn("consistency_score", response.data)

    def test_get_heatmap(self):
        """
        Test retrieving heatmap analytics data.
        """
        response = self.client.get("/api/analytics/heatmap/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)