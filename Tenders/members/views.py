from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def features(request):
  template = loader.get_template('features.html')
  return HttpResponse(template.render({}, request))