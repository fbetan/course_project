from django.test import TestCase
from .models import Politician, Funding
# Create your tests here.

class PoliticianTestCase(TestCase):
    def setUp(self):
        Politician.objects.create(cid="00000",
                                  state="XX",
                                  firstlast="Polly McPolliticia",
                                  lastname = "McPolliticia",
                                  party="X"
                                  )
        


    def test_state_search(self):
        test_count = Politician.objects.filter(state='XX').all().count()
        self.assertEqual(test_count, 1)


        

