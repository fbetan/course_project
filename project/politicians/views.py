from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Politician, Funding

# Create your views here.

def index(request):

    politicians = Politician.objects.all()
    return render(request, "politicians/index.html", {"politicians" : politicians})

def search(request):
    try:
        selected_state = request.POST["state"]
        politicians = Politician.objects.filter(state=selected_state).all()
        count = politicians.count()
        return render(request, 
                      "politicians/search.html", 
                      {"count" : count,
                       "state" : selected_state, 
                       "politicians" : politicians})
        
    except Http404:
        return("Error 404, data may not be available yet. Please try again later")
        
def polinfo(request):
    try:
        selected_name = request.POST['name']
        politicians = Politician.objects.filter(firstlast=selected_name).all()
        return render(request, "politicians/polinfo.html", {"politicians" : politicians})
    
    except Http404:
        return("Error 404, data may not be available yet. Please try again later")

    
