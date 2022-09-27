from django.http import HttpResponse
from django.template import loader
import pandas as pd
import re
def sorts(lis):
 
  data = pd.read_csv('D:/Hackme/Tenders/members/static/tender1.csv')
  d = str(lis['state']) + ',' + ' ' + 'India'
  print(d)
  
  for i,j in data.iterrows():
    
    Title = []
    Location = []
    Price = []
    Deadline = []
    key = []
    Like = []
    Dislike = []
    listing = []
    rating = []
    df = pd.DataFrame({'Title' :Title,'Location':Location,'Price' : Price,'Deadline' :Deadline,'key':key,'Like' :Like,'Dislike' :Dislike,'listing' :listing,'rating' : rating})
    if j['Location'] == d and str(j['rating'])[:1] == lis['rating'] and j['listing'] == lis['listing']:
      Title.append(j['Title'])
      Location.append(j['Location'])
      Price.append(j['Price'])
      Deadline.append(j['Deadline'])
      key.append(j['key'])
      Like.append(j['Like'])
      Dislike.append(j['Dislike'])
      listing.append(j['listing'])
      rating.append(j['rating'])
      print(Title,Location,Price,Deadline)
    else:
      continue
    
    
    
    df.to_csv('tender2.csv', index=False, encoding='utf-8')
    
    
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
  dic = {}
  dic['state'] = state
        
  dic['rating'] = rating
       
  dic['listing'] = listing
       
  dic['listGroupRadio'] =  listGroupRadio
  print(dic)
  data = sorts(dic)
  return HttpResponse(template.render({}, request))


   