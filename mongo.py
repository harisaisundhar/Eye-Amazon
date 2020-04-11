import datetime
import pymongo
import scrap

client = pymongo.MongoClient("mongodb+srv://<user>:<pass>@scrapbook-iydc2.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.Amz

def pushData(details,URL):
    
    ext=scrap.getExt(URL)
    
    new = db[ext]
    ASIN = details["url"][len(details["url"])-10:len(details["url"])]

    try:
        details["date"] = datetime.datetime.utcnow()
        new.update_one({"asin":ASIN}, {"$set": {"asin":ASIN}, "$push":{"details":details}}, upsert=True)
        return True
    except Exception as err:
        print(err)
        return False