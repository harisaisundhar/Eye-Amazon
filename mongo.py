import datetime
import pymongo
import scraper

client = pymongo.MongoClient("mongodb+srv://<user>:<pass>@scrapbook-iydc2.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.Amz

