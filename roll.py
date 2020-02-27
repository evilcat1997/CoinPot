import requests
import json
import threading
import queue

def runNow():
    fff = open("session.txt", "r")
    ck = fff.read()

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

def tempConvert(token,ck):
    url = "https://coinpot.co/api/transactions/service.svc/Convert"
    payload = "{\"request\":{\"fromCurrencyRef\":\"TOKENS\",\"fromAmount\":\""+str(token)+"\",\"toCurrencyRef\":\"DASH\",\"password\":\"Evil1997\",\"twoFactorAuthCode\":\"\"}}"
    headers = {
        'content-type': "application/json; charset=UTF-8",
        'cookie': ck
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    jsonRES = json.loads(response.text)
    r =  jsonRES["d"]["resultDetails"]
    return r
def getToken(ck):
   try:
    url = "https://coinpot.co/api/transactions/service.svc/GetCoinSummary"
    payload = "{\"request\":{\"currencyId\":7}}"
    headers = {
        'content-type': "application/json; charset=UTF-8",
        'cookie': ck
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    jsonRES = json.loads(response.text)
    r =  jsonRES["d"]["currencySummary"]["balance"]
    return int(r)
   except:
    getToken(ck)

def startRoll(i,temp,ck):
    j = Roll(i,temp,ck)
    print("\nTotal: "+str(j["r"]))
    print("========================================================================================================================")
    return int(j["i"])



def multiThread():
    thread = threading.Thread(target=runNow)
    thread.start()

# Start run
multiThread()