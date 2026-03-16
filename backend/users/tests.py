from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status


class AuthTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123"
        )

    def test_jwt_login(self):
        """
        Test that a user can obtain JWT tokens.
        """

        url = "/api/auth/login/"
        data = {
            "username": "testuser",
            "password": "testpassword123"
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)