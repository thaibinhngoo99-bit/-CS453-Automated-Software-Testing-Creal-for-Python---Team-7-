from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

QUIZZES_URL = reverse('questionary:quiz-list')


class PublicQuizzesApiTests(TestCase):
    """Test the publicly available tags API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login required for retrieving quizzes"""
        res = self.client.get(QUIZZES_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)