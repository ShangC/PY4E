"""
Use the below information to test:
    URL:        http://py4e-data.dr-chuck.net/comments_42.xml
    Retrieved:  4189
    Count:      50
    Sum:        2553
"""

import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl 

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    try:
        XmlUrl = input("Enter Location:")
        if len(XmlUrl) < 1:
            break
        print("Retrieving:",XmlUrl)
        XmlData = urllib.request.urlopen(XmlUrl).read()
        print("Retrieved:",len(XmlData),"characters")
        XmlTree = ET.fromstring(XmlData)
        XmlItem = XmlTree.findall("comments/comment")
        print("Count:",len(XmlItem))
        XmlScores =[]
        for item in XmlItem:
            XmlScores.append(int(item.find("count").text))
        print("Sum:",sum(XmlScores))
        break
    except ValueError:
        print("Invalid URL, please try again")