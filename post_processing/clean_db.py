from pymongo import MongoClient
from typing import List

def remove_keys(keys_to_remove: List[str]) -> None:
    client = MongoClient("mongodb://bouman:80um4N!@ec2-15-188-255-64.eu-west-3.compute.amazonaws.com:27017/")
    db = client["bouman_datatank"]
    collection = db["articles"]

    update_op = { "$unset" : { key : 1 for key in keys_to_remove } } 
    
    collection.update_many({}, update_op)

if __name__ == "__main__":
    keys_to_remove = ["meta", "textrazor_response"]
    remove_keys(keys_to_remove)
