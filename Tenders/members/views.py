from django.http import HttpResponse
from django.template import loader
import pandas as pd
import re

    
def index(request):
  template = loader.get_template('index.html')
  
  # get the form data
  
  #f = tell(form)
 
  return HttpResponse(template.render())

def features(request):
  template = loader.get_template('features.html')
  state = request.GET.get('state')
  rating = request.GET.get('rating')
  listing = request.GET.get('listing')
  listGroupRadio = request.GET.get('listGroupRadio')
  
  return HttpResponse(template.render({}, request))

def test(request):
  template = loader.get_template('test.html')
  return HttpResponse(template.render())

   