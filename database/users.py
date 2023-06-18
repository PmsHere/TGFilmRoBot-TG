import pymongo
from info import DATABASE_URI, DATABASE_NAME

dbclient = pymongo.MongoClient(DATABASE_URI)
database = dbclient[DATABASE_NAME]

user_collectionslp = database['usersgftyy']

async def present_in_userbase(user_id : int):
    found = user_collectionslp.find_one({'_id': user_id})
    if found:
        return True
    else:
        return False

async def add_to_userbase(user_id: int):
    user_collectionslp.insert_one({'_id': user_id})
    return

async def get_users():
    user_docs = user_collectionslp.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
        
    return user_ids
    
async def del_from_userbase(user_id: int):
    user_collectionslp.delete_one({'_id': user_id})
    return
