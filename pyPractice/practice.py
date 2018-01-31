# Chapter 11 Exercise
# import re

# x = 'From 90:12:22 shang.chen@wlglobalcorp.com.cn Sat Jan 4 09:14:22 2015'

# y = re.findall('\S+@\S+', x)
# print(y)

# z = re.findall('\S?@\S?', x)
# print(z)

# zz = re.findall('[a-z0-9]', x)
# print(zz)
# print(type(zz))

# zzz = re.findall('\S+?@\S+', x)
# print(zzz)

# zzzz = re.findall('@(\S+)', x)
# print(zzzz)

# a = 'From: Using the : Character'
# b = re.findall('^F.+:', a)
# print(b)

############################################################################
# Chapter 12 Exercise
# this is a test
# this is a test from vscode with git file downloaded from github desktop
#
# import urllib.request
# import urllib.parse
# import urllib.error
# fhand = urllib.request.urlopen('https://en.wikipedia.org/wiki/China')
# for line in fhand:
#     print(line.decode().strip())

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_42.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# # Retrieve all of the anchor tags
# spans = soup('span')
# numbers = []
# for span in spans:
#     numbers.append(int(span.string))
#     print(span)
#     print(span.string)
# print(numbers)
# print(sum(numbers))

# Chapter 12 Exercise
# this is a test
# this is a test from vscode with git file downloaded from github desktop
#
# import urllib.request
# import urllib.parse
# import urllib.error
# fhand = urllib.request.urlopen('https://en.wikipedia.org/wiki/China')
# for line in fhand:
#     print(line.decode().strip())

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import re
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = 'http://py4e-data.dr-chuck.net/comments_42.html'
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

# # Retrieve all of the anchor tags
# spans = soup('span')
# numLst = []
# for span in spans:
#     print(span)
#     x = re.findall('[0-9]+', int(span.string))
#     numLst.append(x)
# print(numLst)
# print(sum(numLst))