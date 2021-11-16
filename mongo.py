import datetime                            # Imports datetime library

import pymongo
from pymongo import MongoClient


client = pymongo.MongoClient("mongodb://hovsep:123456a@cluster0-shard-00-00.zysjb.mongodb.net:27017,cluster0-shard-00-01.zysjb.mongodb.net:27017,cluster0-shard-00-02.zysjb.mongodb.net:27017/testa?ssl=true&replicaSet=atlas-vi7z3w-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

#############################################


print(client.stats)

#################################################

# Show existing database names
print(client.list_database_names())