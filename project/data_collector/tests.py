from django.test import TestCase

from .models import Politician, Funding
from unittest import mock

# Create your tests here.
class DataCollectionTestCase(TestCase):
     def setUp(self):
        self.api_key = "181b03bde6f910748664d4f7c1811fb3"
        self.base_url = "http://www.opensecrets.org/api/?method=getLegislators"
        
#       self.mocktician = mock.Mock(spec=Politician)
#       self.mock_json = {'response':{'legislator':['@attributes':{'cid':'0000','firstlast':'Polly McPoliticia'}]}}
        
#     def _mock_response(
#             self,
#             status=200,
#             content="CONTENT",
#             json_data=None,
#             raise_for_status=None):  
        
#         mock_response = mock.Mock()
#         mock_response.raise_for_status = mock.Mock()
#         if raise_for_status:
#             mock_response.raise_for_status.side_effect = raise_for_status
#         mock_response.status_code = status
#         mock_response.content = content
#         if json_data:
#             mock_response.json_data = mock.Mock(
#                 return_value=json_data
#             )
#         return mock_response
    
#     @mock.patch('requests.get')
#     def test_state_collections(self, mock_get):
#         mock_response = self._mock_response(json_data= = self.mock_json)
#         mock_get.return_value = mock_response
        
#         result = add_politicians("XX")
        
        