import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

while True:
    xmlURL = input("Enter Location:")
    print("Retrieving:",xmlURL)
    xmlData = urllib.request.urlopen(xmlURL).read()
    print("Retrieved:",len(xmlData),"characters")
    xmlTree = ET.fromstring(xmlData)
    xmlItem = xmlTree.findall("comments/comment")
    print("Count:",len(xmlItem))
    scores =[]
    for item in xmlItem:
        scores.append(int(item.find("count").text))
    print("Sum:",sum(scores))
    break
