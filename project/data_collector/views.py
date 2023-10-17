from django.shortcuts import render
import requests
from politicians.models import Politician, Funding
import politicians.templates


# Create your views here.
class API:
    def __init__(self):
        self.api_key = "181b03bde6f910748664d4f7c1811fb3"
        
        
    
    def add_politicians(self,state):
    
        base_url = "http://www.opensecrets.org/api/?method=getLegislators"
        response = requests.get(base_url + f"&id={state}&apikey={self.api_key}&output=json", timeout=120)
        response_list = response.json()['response']['legislator']
        for count, entry in enumerate(response_list, 0):
            attributes = entry['@attributes']
            new_entry = Politician(cid = attributes['cid'],
                                state = state,
                                firstlast = attributes['firstlast'],
                                lastname = attributes['lastname'],
                                party = attributes['party'],
                                office = attributes['office'],
                                gender = attributes['gender'],
                                first_elected = attributes['first_elected'],
                                phone = attributes['phone'],
                                fax = attributes['fax'],
                                website = attributes['website'],
                                webform = attributes['webform'],
                                congress_office = attributes['congress_office'],
                                bioguide_id = attributes['bioguide_id'],
                                votesmart_id = attributes['votesmart_id'],
                                feccandid = attributes['feccandid'],
                                twitter_id = attributes['twitter_id'],
                                youtube_url = attributes['youtube_url'],
                                facebook_id = attributes['facebook_id']
                                    )
            new_entry.save()


    def add_funding_info(self, cid, cycle='2022'):
    
        base_url = "http://www.opensecrets.org/api/?method=candIndustry"
        response = requests.get(base_url + f"&apikey={self.api_key}&cid={cid}&cycle={cycle}&output=json", 
                                timeout=120)
        response_list = response.json()['response']
        cand_info = response_list['industries']['@attributes']
        response_industries = response_list['industries']['industry']
        for count, entry in enumerate(response_industries, 0):
            attributes = entry['@attributes']
            new_entry = Funding(
                cid = cand_info['cid'],
                cand_name = cand_info['cand_name'],
                cycle = cycle,
                origin = cand_info['origin'],
                source = cand_info['source'],
                industry_code = attributes['industry_code'],
                industry_name = attributes['industry_name'],
                indivs = attributes['indivs'],
                pacs = attributes['pacs'],
                total = attributes['total']
            )
            new_entry.save()

    
def index(request):
    politicians = Politician.objects.all()
    return render(request, "data_collector/collect_index.html",
                  {"politicians" : politicians})

def collect(request):
    try:
        selected_state = request.POST["state"]
        current_count = (Politician.objects.filter(state=selected_state)).count()
        if current_count != 0:
            current_politicians = Politician.objects.filter(state=selected_state)
            return render(request, 'politicians/search.html', {"count" : current_count, "state" : selected_state, "politicians" : current_politicians})

        api = API()
        api.add_politicians(selected_state)
        politicians = Politician.objects.filter(state=selected_state)
        count = (Politician.objects.filter(state=selected_state)).count()
        total_count = Politician.objects.count()
        return render(request, 'data_collector/collection.html', {"count" : count, "state" : selected_state, "politicians" : politicians, "total_count" : total_count})

    except KeyError:
        return "idunno"

def collect_industry(request):
    try:
        selected_cid = request.POST["cid"]
        current_count = (Funding.objects.filter(cid=selected_cid)).count()
        if current_count != 0:
            funding_info = Funding.objects.filter(cid=selected_cid).all()
            name = funding_info[0].cand_name
            return render(request, 'data_collector/fundinginfo.html',
                          {"name" : name,
                          "funding_info" : funding_info})
        api = API()
        api.add_funding_info(selected_cid)
        funding_info = Funding.objects.filter(cid=selected_cid).all()
        name = funding_info[0].cand_name
        return render(request, 'data_collector/fundinginfo.html',
                          {"name" : name,
                          "funding_info" : funding_info})
    except KeyError:
        return 'ialsodunno'