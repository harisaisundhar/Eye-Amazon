import datetime
import pymongo
import scrap

client = pymongo.MongoClient("<connection string>")
db = client.Amz

def pushData(details,URL):
    
    ext=scrap.getExt(URL)
    
    new = db[ext]
    ASIN = details["Url"][len(details["Url"])-10:len(details["Url"])]

    try:
        details["Date"] = datetime.datetime.utcnow()
        new.update_one({"asin":ASIN}, {"$set": {"asin":ASIN}, "$push":{"details":details}}, upsert=True)
        return True
    except Exception as err:
        print(err)
        return False