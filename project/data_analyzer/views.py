from django.shortcuts import render
from politicians.models import Politician, Funding
import politicians.templates


# Create your views here.

def index(request):
    politicians = Politician.objects.all()
    fundings = Funding.objects.all()
    return render(request, "data_analyzer/analyze_index.html",
                           {"politicians" : politicians,
                           "fundings" : fundings})

def analyze(request):
        try:
            selected_cid = request.POST['cid']
            fundings = Funding.objects.filter(cid=selected_cid).all()
            name = fundings[0].cand_name
            return render(request, 'data_analyzer/fundinginfo.html',
                                   {"name" : name,
                                   "fundings" : fundings})
        except ValueError:
            print("Not found!")

def analyze_industry(request):

    try:
        selected_industry_code = request.POST['industry_code']
        fundings = Funding.objects.filter(industry_code=selected_industry_code).all()
        industry_name = fundings[0].industry_name
        return render(request, 'data_analyzer/analyze_industry.html',
                               {"industry_name" : industry_name,
                               "fundings":fundings})

    except ValueError:
         return 'I a dumb'