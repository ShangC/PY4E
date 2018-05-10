import urllib
import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
urlCount = int(input("Enter Count:"))
urlPosition = int(input("Enter Position:"))
while urlCount > 0:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")
    tags = soup("a")
    print("Retrieving:",url)
    url = tags[urlPosition-1].get("href", None)
    urlCount = urlCount - 1
    
