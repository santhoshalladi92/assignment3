import pymongo
import os
#import demjson
from pymongo import MongoClient
client = MongoClient()
db = client.cog_db
collection = db.cog_data
#post1=""
#fp = open("/home/santhosh/assignment2/a2.json", "r")            
#for line in fp:
#	post1=post1+line
#post = demjson.encode(post1)

#posts=db.posts
#post_id = posts.insert(post)
#post_id
os.system("mongoimport -d cog_db -c final /home/santhosh/assignment2/a2.json --jsonArray")
