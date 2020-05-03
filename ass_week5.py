from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url=input("Enter location: ")
print("Retrieving ",url)
data=urlopen(url,context=ctx).read()
print("Retrieved ",len(data),"characters")
tree=ET.fromstring(data)
tags=tree.findall('comments/comment')
print("Count: ",len(tags))
sum=0
for tag in tags:
    sum+=int(tag.find('count').text)
print("Sum: ",sum)
