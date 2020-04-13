import mongo
import scrap
import time
import mail
from email_validator import validate_email, EmailNotValidError

URL = "https://www.amazon.in/Amazon-Brand-Solimo-Activated-Charcoal/dp/B07W4WSY1R?ref_=Oct_MWishedForC_1374295031_0&pf_rd_r=27XEPK5SKGH9Y0T48VYY&pf_rd_p=88aa8f1d-3713-510e-a108-29e72fb545b8&pf_rd_s=merchandised-search-8&pf_rd_t=101&pf_rd_i=1374295031&pf_rd_m=A1VBAL9TL5WCBF"

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