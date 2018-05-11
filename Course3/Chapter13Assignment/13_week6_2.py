''' 
Use the following university names to find place id: 
    University Name:    University of Buenos Aires
    Place ID:           ChIJTaQ4qcD-Lw0RqQq2VIWolIw

    University Name:    South Federal University
    Place ID:           ChIJJ8oO7_B_bIcR2AlhC8nKlok
'''

import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

ServiceUrl = "http://py4e-data.dr-chuck.net/geojson?"

while True:
    JsonUrl = input("Enter Location:")
    if len(JsonUrl) < 1:
        break
    
    ApiUrl = ServiceUrl + urllib.parse.urlencode({"address": JsonUrl})

    print("Retrieving", ApiUrl)
    ApiData = urllib.request.urlopen(ApiUrl).read().decode()
    print("Retrieved",len(ApiData),"characters")

    try:
        js = json.loads(ApiData)
    except:
        js = None

    if not js or "status" not in js or js["status"] != "OK":
        print("==== Failure To Retrieve ====")
        print(ApiData)
        continue

    print(json.dumps(js, indent=4))

    PlaceID = js["results"][0]["place_id"]
    print("Place ID:", PlaceID)