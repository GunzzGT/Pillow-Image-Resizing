from pymongo import MongoClient
# python -m pip install "pymongo[srv]"
# python -m pip install python-dateutil
CONNECTION_STRING = "mongodb://localhost:27017/"


def get_database():
    client = MongoClient(CONNECTION_STRING)
    return client['user_shopping_list']

def close_database():
    client = MongoClient(CONNECTION_STRING)
    print('connection_closed')
    client.close()

# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # Get the database
    dbname = get_database()