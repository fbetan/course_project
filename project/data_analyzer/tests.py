from django.test import TestCase
from .models import Politician, Funding
# Create your tests here.


class AnalyzeTestCase(TestCase):
    def setUp(self):
        Politician.objects.create(cid='00000', 
                                  firstlast='Polly McPolliticia',
                                  lastname='McPolliticia',
                                  party='X')
        
        Funding.objects.create(cid='00000',
                               cand_name='Polly McPolliticia (X)',
                               total = '1000000000000000002')
        
    def test_analyst(self):
        test_cid = '00000'
        test_politician= Politician.objects.filter(cid=test_cid)
        test_firstlast = test_politician[0].firstlast
        fundings = Funding.objects.filter(cid=test_cid).all()
        name = fundings[0].cand_name
        assert(name == 'Polly McPolliticia (X)')
        assert(fundings[0].total == '1000000000000000002')
        assert(test_firstlast == 'Polly McPolliticia')
            