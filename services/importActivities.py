import pandas as pd
from pymongo import MongoClient
import json



def import_content():
    client = MongoClient("mongodb+srv://niobrara:niobrara123@adaptiveblinddateapp-hdqaj.mongodb.net/test")
    db = client.timble
    collection_name = 'Activities' 
    db_cm = db[collection_name]
    dataset=pd.read_csv('/Users/shuchitakapoor/Downloads/Activities.csv')
    data_json = json.loads(dataset.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json)

if __name__ == "__main__":
  import_content()