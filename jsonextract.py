from urllib.request import urlopen
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location - ')
html = urlopen(url,context=ctx).read()
print('Retrieving',url)
info = json.loads(html)
sum = 0
for item in info['comments']:
    sum += int(item['count'])
print('Count:',len(info['comments']))
print('Sum:',sum)
