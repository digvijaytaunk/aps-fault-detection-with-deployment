
import pymongo

from sensor import MONGO_CONNECTION_STRING

mongo_client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
