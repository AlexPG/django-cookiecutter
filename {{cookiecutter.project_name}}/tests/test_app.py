from django.test import TestCase
from django.urls import reverse

class TestApp(TestCase):
    
    def test_app_is_running(self):
        url = reverse('home')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
