import urllib
import urllib.request
import urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

TxtUrl = input("Enter Location:")
TxtData = urllib.request.urlopen(TxtUrl).read()
print(TxtData)
