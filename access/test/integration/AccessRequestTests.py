from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AccessRequestTests(APITestCase):
    def test_get_auth_token_passes(self):

        """
        Ensure we can get an auth token with valid member_id, machine_id,
        and access level
        """
        url = reverse('access_request')
        data = {'member_card_id': '0xFFEE0011', 'machine_id': '0x6655FF33'}
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
