from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
pos=input("Enter the position of the link--")
pos=int(pos)
rep=input("Enter the repetetions of this process--")
rep=int(rep)
while rep>0:
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    count=0
    for tag in tags:
        count+=1
        if count==pos:
            href=tag.get('href', None)
            print("\nname--",tag.contents[0])

    url=href
    rep-=1
