from django.urls import reverse
from rest_famework import status
from rest_framework.test import APITestCase


class ProfileTests(APITestCase):
    def test_get_profiles(self):
        """
        Ensure we can get a profile from the api
        """

        url = reverse('Profile-get')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
