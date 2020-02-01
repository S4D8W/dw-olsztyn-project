import requests
from pprint import pprint
from bs4 import BeautifulSoup
import json
import codecs
import Deputy
import urllib3
import base64
# Deputy == poseł

def GetDeputyContentHtml(xDputyUrl):
    
    pRequest = requests.get(xDputyUrl)
    if(pRequest.status_code> 200):
        print(f"[DEBUG]requst url:{xDputyUrl} return status code {pRequest.status_code}")
    pSoup = BeautifulSoup(pRequest.text, "lxml")
    pContent = pSoup.find('div',{'id':'contentBody'})
   

    return pContent

def ParseDeputy(xContent):
    pMainArr ={}
    pMainData = xContent.find('ul',{'class':'data'})
    pImageSRC = xContent.find('img')['src']
    pImageBase64 = GetImagoFromSrc(pImageSRC)
    pMainArr['imgb64']=pImageBase64
    #Data
    i=1
    for pRow in pMainData.findAll("li"):
        foo= pRow.find('p',{'class':'right'}).text
        pMainArr[i]=foo
        i +=1
    #Cv
    pCvDiv = xContent.find('div',{'class':'cv'})
    for pRow in pCvDiv.findAll("li"):
        foo= pRow.find('p',{'class':'right'}).text
        pMainArr[i]=foo
        i +=1


def GetImagoFromSrc(xSrc):
     pBase64 = base64.b64encode(requests.get(xSrc).content)
     return pBase64

def IdGenertator(xNumber):
    pID=""
    if xNumber <= 9:
        pID="00"+str(xNumber)
        return pID
    if xNumber <100:
        pID ="0"+str(xNumber)
        return pID
    if xNumber >= 100:
        pID = str(xNumber)
        return pID
    




def PageNawigation():
    i=1
    
    while i <2:
        pID = IdGenertator(i)
        pDeputy = f"https://www.sejm.gov.pl/Sejm9.nsf/posel.xsp?id={pID}&type=A"
        pConntent = GetDeputyContentHtml(pDeputy)
        ParseDeputy(pConntent)
        i +=1

PageNawigation()