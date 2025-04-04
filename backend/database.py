from pymongo import MongoClient

# Change URI for MongoDB Atlas if needed
MONGO_URI = "mongodb://localhost:27017"

client = MongoClient(MONGO_URI)
db = client["smartshopping"]

def get_db():
    return db
