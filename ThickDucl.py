import requests
from pprint import pprint
from bs4 import BeautifulSoup
import json
import codecs
import Deputy

# Deputy == poseł

def GetDeputyContentHtml(xDputyUrl):
    
    pRequest = requests.get(xDputyUrl)
    if(pRequest.status_code> 200):
        print(f"[DEBUG]requst url:{xDputyUrl} return status code {pRequest.status_code}")
    pSoup = BeautifulSoup(pRequest.text, "lxml")
    pContent = pSoup.find('div',{'id':'contentBody'})
   

    return pContent

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
        GetDeputyContentHtml(pDeputy)
        i +=1

PageNawigation()