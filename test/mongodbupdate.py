from mongodbcreate import get_database
from mongodbcreate import close_database

dbname = get_database()
collection_name = dbname["user_1_items"]

close_database()

collection_name.update_one(
    {"_id": "U1ITtest1"},
    {"$set": {"id2": "test3", "bebas": "test ga bebas"}}
)