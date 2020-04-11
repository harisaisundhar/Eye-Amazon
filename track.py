import mongo
import scrap
import time
import mail
from email_validator import validate_email, EmailNotValidError

URL = "https://www.amazon.in/Himalaya-Pure-Hands-Purifying-Tulsi/dp/B0828XSF6L/ref=sr_1_2?dchild=1&keywords=sanitizer+spray+for+hand&qid=1586586172&sr=8-2"

def myurl():
    return URL

def run():
    escapelimit=int(input("Enter the amount to alert : "))
    mailid=input("enter the mailid : ")

    try:
        v = validate_email(mailid) 
        mailid = v["email"] 
    except EmailNotValidError as e:
        print(str(e))
        
    data = scrap.getProdDetails(URL)
    result = ""
    if data is None:
        result = "Error in scrapping"
    else:
        inserted = mongo.pushData(data,URL)
        if inserted:
            result = "Check Done.. Next check in 30 mins....."
        else:
            result = "Error in Database Insertion"
        cost=int(data["Price"])
        if cost<=escapelimit:
            mail.send_mail(data["Url"],cost,data["Name"],mailid)
            print('Eyedropper sent a mail')
    return result

while True:
    print(run())
    time.sleep(60)