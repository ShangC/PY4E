import urllib
import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    try:
        url = input("Enter URL: ")
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")
        scores = []
        spans = soup("span")

        for span in spans:
            scores.append(int(span.string))
        print("Count:",len(scores))
        print("Sum:",sum(scores))
        break
    except ValueError:
        print("Error URL, please enter again")
