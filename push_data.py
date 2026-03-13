import os
import json
import sys

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URI = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URI)
import certifi
ca=certifi.where()
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkSecurityData:
    def __init__(self):
        try:
            self.client = pymongo.MongoClient(MONGO_DB_URI, tlsCAFile=ca)
            self.db = self.client['NetworkSecurity']
            self.collection = self.db['network_traffic']
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    def cv_to_json(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)    
    def insert_data(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URI)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
if __name__=="__main__":
    file_path="Network_Data\phisingData.csv"
    DATABASE="NetworkSecurity"
    COLLECTION="network_data"
    networkoj=NetworkSecurityData()
    records=networkoj.cv_to_json(file_path)
    no_of_records=networkoj.insert_data(records,DATABASE,COLLECTION)   
    print(f"{records} ")
    print(f"{no_of_records} ")   
