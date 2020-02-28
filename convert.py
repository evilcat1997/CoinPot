# importing the requests library 
import requests
import json
#from threading import Thread
import threading
import queue


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
def tempConvert2(token,ck):
    url = "https://coinpot.co/api/transactions/service.svc/Convert"
    payload = "{\"request\":{\"fromCurrencyRef\":\"DASH\",\"fromAmount\":\""+str(token)+"\",\"toCurrencyRef\":\"TOKENS\",\"password\":\"Evil1997\",\"twoFactorAuthCode\":\"\"}}"
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

def convertNow():
    fff = open("session.txt", "r")
    ck = fff.read()
    
    try:
        aaa = 0
        bch = 0,0
        text = ""
        while aaa < 10:
            i = getToken(ck)
            if i > 500:
                text = tempConvert(400,ck)
                print("##################################################################################")
                print(text)
                print("##################################################################################")
            if i > 400:
                text = tempConvert(300,ck)
                print("##################################################################################")
                print(text)
                print("##################################################################################")
            if i > 300:
               text = tempConvert(200,ck)
               print("##################################################################################")
               print(text)
               print("##################################################################################")
            if i > 200:
               text = tempConvert(150,ck)
               print("##################################################################################")
               print(text)
               print("##################################################################################")
            if i > 100:
               text = tempConvert(10,ck)
               print("##################################################################################")
               print(text)
               print("##################################################################################")
            if i > 60:
               text = tempConvert(1,ck)
               print("##################################################################################")
               print(text)
               print("##################################################################################")
            if i < 50:
               text = tempConvert2(0.00005,ck)
               print("##################################################################################")
               print(text)
               print("##################################################################################")
            else:
               text = ""
    except:
        convertNow()
        
# Start        
convertNow()