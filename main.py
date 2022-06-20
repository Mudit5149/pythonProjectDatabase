import pymongo

client=pymongo.MongoClient()

mydb=client["pythondb"]

mycol=mydb["Product"]

# data={'Name':'Mobile', 'Price':'2300'}
# mycol.insert_one(data)

datalist=[{'Name':'Laptop','Pice':'25000'},{'Name':'tablet','Price':'30000'}]
x=mycol.insert_many(datalist)
for x in mycol.find():
 print(x)