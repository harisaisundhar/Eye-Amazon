
from bs4 import BeautifulSoup
from price_parser import Price
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
        
def getPrice(cost):

    price = Price.fromstring(cost)
    #print(price.amount_float)
    return price.amount_float

def getCurrency(cost):
    price = Price.fromstring(cost)
    #print(price.currency)
    return price.currency


def getProdDetails(data):

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"
    }
    details = {"Name": "",
               "Price": 0,
               "Currency": None ,
               "Deal": True,
               "Url": ""
               };
               
    url = getURL(data)
    if url is None:
        details = None
    else:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html5lib")
        title = soup.find(id="productTitle")
        price = soup.find(id="priceblock_dealprice")
        if price is None:
            price = soup.find(id="priceblock_ourprice")
            details["Deal"] = False
        if title is not None and price is not None:
            details["Name"] = title.get_text().strip()
            details["Price"] = getPrice(price.get_text())
            details["Currency"]=getCurrency(price.get_text())
            details["Url"] = url
        else:
            details = None
    print(details)
    #return details