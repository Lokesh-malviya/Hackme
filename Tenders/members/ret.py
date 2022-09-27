import re
url = "GET /?state=&rating=4&listing=BSE&listGroupRadio=50-80 HTTP/1.1"

f = url.replace("GET","")
pat = r'[/?\1.1 ]'
f = re.sub(pat,'',f)
f = f.replace("HTTP",'')
f  = f.split('&')
dic = {}
print(f)
for i in f:
    if i == 'state=' or len(i) ==len('rating=') or i=='listing=' or i == 'listGroupRadio=':
      continue
        
    else:
        if i[0:6] == 'state=':
            dic['state'] = i[6:]
        elif i[0:7] == 'rating=':
            dic['rating'] = i[7:]
        elif i[0:8] == 'listing=':
            dic['listing'] = i[8:]
        elif i[0:15] == 'listGroupRadio=':
            dic['listGroupRadio'] = i[15:]
        
print(dic)