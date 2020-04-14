import datetime
import pymongo
import scrap
from dotenv import load_dotenv
import os
import json
import pandas as pd
import matplotlib.pyplot as plt

load_dotenv()
def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def pushData(details,URL):
    client = pymongo.MongoClient(os.getenv("MONGO_STRING"))
    db = client.Amz
    ext=scrap.getExt(URL)
    new = db[ext]
    ASIN = details["Url"][len(details["Url"])-10:len(details["Url"])]

    try:
        print(datetime.datetime.utcnow())
        details["Date"] = datetime.datetime.utcnow()
        new.update_one({"asin":ASIN}, {"$set": {"asin":ASIN}, "$push":{"details":details}}, upsert=True)
        return True
    except Exception as err:
        print(err)
        return False
    
def getHistory(URL):

    client = pymongo.MongoClient(os.getenv("MONGO_STRING"))
    db = client.Amz
    ext=scrap.getExt(URL)
    asin=scrap.getAsin(URL)
    new = db[ext]
    try:
        find = new.find_one({"asin": asin}, {"_id": 0})
        if find:
            d=find
            data=json.dumps(d, default = myconverter)
            data = json.loads(data)
            print(data)
            dates=[]
            values=[]
            curr=[]
            for i in data['details']:
                dates.append(i['Date'])
                values.append(i['Price'])
                curr.append(i['Currency'])
            
            data = {'a': dates,'b':values}
            df = pd.DataFrame({'dates':dates, 'values':values})
            df['dates']  = [pd.to_datetime(i) for i in df['dates']]

            #print(df.sort_values(by='dates'))
            plt.xlabel('Date')
            plt.ylabel('Cost in '+curr[0])
            plt.plot(dates, values)
        else:
            raise Exception("Not found")
    except Exception as identifier:
        print(identifier)
        return None