from django.test import TestCase
from django.urls import reverse

class TestViews(TestCase):
    def test_index(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, 'Hello World3!')
