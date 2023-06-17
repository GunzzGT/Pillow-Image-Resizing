from mongodbcreate import get_database

dbname = get_database()
collection_name = dbname["user_1_items"]
# table name

cursor = collection_name.find()
for doc in cursor:
    print(doc)

from mongodbcreate import close_database

test = collection_name.find({}, {'_id': 0, 'item_name': 1})

for doc in test:
    print(doc)

x = collection_name.find_one()
print(x['item_name'])

myquery = {'item_name': 'Bread'}
mydoc = collection_name.find(myquery)

for y in mydoc:
    print(y)

close_database()
