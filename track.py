import mongo
import scrap
import time
import mail
from email_validator import validate_email, EmailNotValidError

URL = ""
escapelimit=0
mailid=""

def setURL(url):
    global URL
    URL=url

def setEscape(lim):
    escapelimit=lim

def setMail(ids):
    try:
        v = validate_email(ids) 
        ids = v["email"] 
    except EmailNotValidError as e:
        print(str(e))
    mailid=ids

def myurl():
    return URL

def run():
    details = {"Title":"",
               "Result":"",
               "Cost": 0,
               "Curr": None
               };
    data = scrap.getProdDetails(URL)
    details["Cost"]=data["Price"]
    details["Curr"]=data["Currency"]
    details["Title"]=data["Name"]
    if data is None:
        details["Result"] = "Error in scrapping"
    else:
        inserted = mongo.pushData(data,URL)
        if inserted:
            details["Result"] = "Check Done.. Next check in 30 mins....."
        else:
            details["Result"] = "Error in Database Insertion"
        cost=int(data["Price"])
        if cost<=escapelimit:
            mail.send_mail(data["Url"],cost,data["Name"],mailid)
            print('Eyedropper sent a mail')
    return details

def tracker(url):
    setURL(url)
    return run()