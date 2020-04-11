import mongo
import scrap
import time
import mail

URL = "https://www.amazon.com/Daily-Face-Cover-Pack-10/dp/B086QLB6SK/ref=sr_1_1?dchild=1&keywords=masks&qid=1586575883&sr=8-1&th=1"
escapelimit=1000
mailid=input("enter the mailid : ")
def myurl():
    return URL

def run():
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