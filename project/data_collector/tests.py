from django.test import TestCase
from .views import API, index, collect, collect_industry
from .models import Politician, Funding
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import MagicMock


# Create your tests here.
class DataCollectionTestCase(TestCase):
    def setUp(self):
        self.test_api = API()
    
    def test_api_key(self):
        assert(self.test_api.api_key == "181b03bde6f910748664d4f7c1811fb3")

        