'''
Use the below information to test the code:
    URL:        http://py4e-data.dr-chuck.net/comments_42.json
    Retrieved:  2733
    Count:      50
    Sum:        2553

    URL:        http://py4e-data.dr-chuck.net/comments_44137.json
    Retrieved:  
    Count:      50
    Sum:        
'''

import json
import urllib.request
import urllib.parse
import urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    try:
        jsonURL = input("Enter Location:")
        print("Retrieving", jsonURL)
        jsonData = urllib.request.urlopen(jsonURL).read()
        print("Retrieved",len(jsonData),"characters")
        jsonInfo = json.loads(jsonData)
        #print(jsonInfo)
        print("Count:",len(jsonInfo["comments"]))
        jsonCount = []
        for item in jsonInfo["comments"]:
            jsonCount.append(int(item["count"]))

        print("Sum:",sum(jsonCount))
        break
        
    
    except ValueError:
        print("Invalid URL, please enter again")