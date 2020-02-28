import requests
import json
import threading
import queue
from urllib.request import urlopen

fff = open("path.txt", "r")
ffff = fff.read()
data = urlopen(ffff).read()
ck = data

def runNow():
    try:
        ee = 0
        i = 0
        temp = 1
        while ee < 10 :
            i = startRoll(i,temp,ck)
            temp += 1
    except:
       runNow()

def Roll(tempRes,tt,ck):
    url = "https://coinpot.co/api/games/service.svc/PerformRoll"
    a = 0
    if(tempRes == 2):
        a = 0 
    else:
        a = 1
    payload = "{\"request\":{\"highLow\":"+str(a)+",\"multiplier\":2,\"clientSeed\":\"b2e5c55a4988\",\"stake\":1}}"
    headers = {
        'content-type': "application/json; charset=UTF-8",
        'cookie': ck
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    jsonRES = json.loads(response.text)
    print("Roll "+str(tt))
    print(response.text)
    i =  jsonRES["d"]["roll"]["profit"]
    r =  jsonRES["d"]["tokenBalance"]
    return {"i":i,"r":r}

def startRoll(i,temp,ck):
    j = Roll(i,temp,ck)
    print("\nTotal: "+str(j["r"]))
    print("========================================================================================================================")
    return int(j["i"])


#start
runNow()