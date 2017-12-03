# import pandas as pd
# import numpy as np
# import html5lib
# import quandl
#
# internet = pd.read_html(r'https://de.wikipedia.org/wiki/Liste_der_NATO-L%C3%A4ndercodes')
# df_countries = internet[0]
#
# #cleansing
# col_rename = {0:'2digit',1:'3digit',2:'country',3:'Land',4:'comment'}
# df_countries.rename(columns=col_rename, inplace=True)
# df_countries = df_countries[1:]
#
# # extracting data via quandl online
# api_key = open('D:\Python\Quandl_API.txt','r').read()
# df = quandl.get('FMAC/30US',authoken=api_key)
# df.head()
#
# import urllib
# import re
#
# urls = ['http://google.com','http://nytimes.com','http://CNN.com','https://finance.yahoo.com']
# i = 0
# regex = '<title>(.+?)</title>'
# pattern = re.compile(regex)
#
# while i < len(urls):
#     htmlfile = urllib.urlopen(urls[i])
#     htmltext = htmlfile.read()
#     titles = re.findall(pattern, htmltext)
#     print titles[0:100]
#     i+=1
#
# # scraping stock prices
# import urllib
# import re
#
# htmlfile = urllib.urlopen('http://finance.yahoo.com/q?s=AAPL&ql=1')
# htmltext = htmlfile.read()
# regex = '<span id="yfs_184_aapl">(.+?)</span>'
# pattern = re.compile(regex)
# price = re.findall(pattern, htmltext)
# print price
#
# symbol_list = ['aapl','GOOGL','HPQ']
#
# i = 0
#
# while i < len(symbol_list):
#     htmlfile = urllib.urlopen('https://finance.google.com/finance?q=' + symbol_list[i]+ '&ei=X8fnWanDAcnsswHky5m4Bg')
#     htmltext = htmlfile.read()
#     regex = '<span id="ref_22144_l">(.+?)</span>'
#     pattern = re.compile(regex)
#     price = re.findall(pattern, htmltext)
#     print price
#     i+=1

import pandas as pd

symbol_list = ['aapl','googl']
df = pd.DataFrame(columns=['Description','Values','symbol'])

i = 0
while i < len(symbol_list):
    url = 'https://finance.google.com/finance?q='+symbol_list[i]+'&ei=2s_nWcmFIIXDsQGWmb3oAQ'
    data = pd.read_html(url)
    df1 = data[0]
    df1.rename(columns={0:'Description',1:'Values'}, inplace=True)
    df1['symbol'] = symbol_list[i]
    df = df.append(df1)
    i+=1

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com',80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if(len(data) < 1):
        break
    print data

mysock.close()

import urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1
print counts

fhand = urllib.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print line.strip()

# work with urllib and beautifulSoup to get a web crawler return list of links
import urllib
from BeautifulSoup import *
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# retrieve a list of anchor tags
# Each tag is like a dictionary of HTML attributes

tags = soup('a')                    # retrieve a list of anchor tags <a href = ...>
for tag in tags:                    # loop through list of tags
    print tag.get('href', None)     # if no href exists then return None


import telnetlib
