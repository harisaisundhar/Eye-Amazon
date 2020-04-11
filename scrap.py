
from bs4 import BeautifulSoup
import requests

def getURL(data):
    
    coun = data.find("www.amazon.")
    length = len(data)
    if coun != -1:
        ins = data.find("/dp/")
        if ins != -1:
            ine = ins + 14
            temp = data[ins:ine]
        else:
            ins = data.find("/gp/")
            if ins != -1:
                ine = ins + 22
                temp = data[ins:ine]
            else:
                return None
            
        short = data[coun:length]
        fi = short.find("/")
        url = "https://" + short[:fi] + temp
        #print(url)
    
    else:
        url = None
    
    return url
        
def getExt(data):
    
    ind = data.find("www.amazon.")
    length = len(data)
    shorturl = data[ind:length]
    fi = shorturl.find("/")
    ext = shorturl[11:fi]
    #print(ext)
    
    return ext
