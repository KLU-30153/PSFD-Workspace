import pymongo
from pymongo import MongoClient
    #URl to connect DB
c1 = pymongo.MongoClient("mongodb://127.0.0.1:27017")
print(c1.list_database_names())
    #specifying the DB name
database_name = "PFSD1"
student1 = c1[database_name]
    #specifying the Collection name
collection_name = "PFSD"
obj1 = student1[collection_name]
    #Insert Data
document = {"Name": "Dhoni", "Roll No": 100,"Branch": "CSE" }
obj1.insert_one(document)
document = {"Name": "MEGHA VAMSI KIRAN", "Roll No": 153,"Branch": "CSE" }
obj1.insert_one(document)
print("Inserted Data - 1 Successfully")
#document = { "Name": "MEGHA VAMSI KIRAN", "Roll No": 110, "Branch":"CSE"}
