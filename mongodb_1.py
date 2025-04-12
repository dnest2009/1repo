import argparse
from bson.objectid import ObjectId

# підключення до бази даних

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://user:1234@cluster0.mv5ebgc.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.web

parser = argparse.ArgumentParser(description='Server Cats Enterprise')
parser.add_argument('--action',help="create, update, find, read ,delete") #CRUD action
parser.add_argument('--id')
parser.add_argument('--name')
parser.add_argument('--age')
parser.add_argument('--features', nargs='+')
arg = vars(parser.parse_args())
action = arg.get('action')
pk = arg.get('id')
name = arg.get('name')
age = arg.get('age')
features = arg.get('features')

def find():
    return db.cats.find()

def create(name, age, features):
    r = db.cats.insert_one({
        "name": name,
        "age": age,
        "features": features
    })
    return r

def update(pk,name, age, features):
    r = db.cats.update_one({"_id": ObjectId(pk)}, {
        "$set": {
            "name": name,
            "age": age,
            "features": features }
    })
    return r

def delete(pk):
    return db.cats.delete_one({"_id": ObjectId(pk)})

def main():
    match action:
        case 'create':
            r = create(name, age, features)
            print(r)
        case 'read':
            r = find()
            print([e for e in r])
        case 'update':
            r = update(pk,name, age, features)
            print(r)
        case 'delete':
            r = delete(pk)
            print(r)
        case _:
            print('Unknown command')

if __name__ == '__main__':
    main()

