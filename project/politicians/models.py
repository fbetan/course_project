from django.db import models
from django.urls import reverse

# Create your models here.

class Politician(models.Model):
    cid = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    firstlast = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    office = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    first_elected = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    webform = models.CharField(max_length=100)
    congress_office = models.CharField(max_length=100)
    bioguide_id = models.CharField(max_length=100)
    votesmart_id = models.CharField(max_length=100)
    feccandid = models.CharField(max_length=100)
    twitter_id = models.CharField(max_length=100)
    youtube_url = models.CharField(max_length=100)
    facebook_id = models.CharField(max_length=100)
    
    def get_absolute_url(self):
        return reverse("politicians:search", kwargs={"state":self.state})

class Funding(models.Model):
    cid = models.CharField(max_length=100)
    cand_name = models.CharField(max_length=200)
    cycle = models.CharField(max_length=4, default='2022')
    origin = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    industry_code = models.CharField(max_length=6)
    industry_name = models.CharField(max_length=200)
    indivs = models.CharField(max_length=12)
    pacs = models.CharField(max_length=12)
    total = models.CharField(max_length=12)

    def get_absolute_url(self):
        return reverse("collection:collect_industry", kwargs={"cid":self.cid})