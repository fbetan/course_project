from django.shortcuts import render
from django.http import HttpResponse, Http404
from politicians.models import Politician, Funding
import politicians.templates
from data_collector.views import API, collect, collect_industry


def index(request):
    politicians = Politician.objects.all()
    fundings = Funding.objects.all()
    return render(request, "data_analyzer/analyze_index.html",
                           {"politicians" : politicians,
                           "fundings" : fundings})

def analyze(request):
    try:
        selected_cid = request.POST['cid']
        current_count = (Funding.objects.filter(cid=selected_cid).all()).count()
        if current_count == 0:
            collect_industry(request)
        fundings = Funding.objects.filter(cid=selected_cid).all()
        name = fundings[0].cand_name
        return render(request, 'data_analyzer/fundinginfo.html',
                                   {"name" : name,
                                   "fundings" : fundings})    
    except Http404:
        return("Error 404, data may not be available yet. Please try again later")
        
def analyze_industry(request):

    try:
        selected_industry_code = request.POST['industry_code']
        fundings = Funding.objects.filter(industry_code=selected_industry_code).all()
        industry_name = fundings[0].industry_name
        republican_contributions = []
        democratic_contributions = []
        third_contributions = []
        for funding in fundings:
            if '(R)' in funding.cand_name:
                republican_contributions.append(int(funding.total))
            elif '(D)' in funding.cand_name:
                democratic_contributions.append(int(funding.total))
            else:
                third_contributions.append(int(funding.total))
        republican = sum(republican_contributions)
        democratic = sum(democratic_contributions)
        third = sum(third_contributions)
        sum_republican = "{:,}".format(republican)
        sum_democratic = "{:,}".format(democratic)
        sum_third = "{:,}".format(third)

        return render(request, 'data_analyzer/analyze_industry.html',
                               {"industry_name" : industry_name,
                               "fundings":fundings,
                               "sum_republican":sum_republican,
                               "sum_democratic":sum_democratic,
                               "sum_third":sum_third})

    except Http404:
        return("Error 404, data may not be available yet. Please try again later")
