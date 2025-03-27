from django.test import TestCase
from .models import Client

class ClientModelTests(TestCase):
    def test_string_representation(self):
        client = Client(first_name="John", last_name="Doe")
        self.assertEqual(str(client), "John Doe")