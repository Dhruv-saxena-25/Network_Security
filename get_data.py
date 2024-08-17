import sys
import json
from typing import List, Tuple, Optional
import os
import pandas as pd
import numpy as np
import pymongo
import certifi
from dotenv import load_dotenv

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

load_dotenv()
ca = certifi.where()

MONGO_DB_URL = os.getenv('MONGO_DB_URL')

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json_convertor(self, file_path):
        """
        it read the data from the source
        """
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop= True, inplace= True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def pushing_data_to_mongodb(self,records,database_name: str,collection_name: str):
        try:
            if database_name is not None:
                
                self.records=records
                self.database_name=database_name
                self.collection_name=collection_name
                
                self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
                
                self.mongo_client.admin.command('ping')
                print("Pinged your deployment. You successfully connected to MongoDB!")
                
                self.database = self.mongo_client[self.database_name]
            
                self.collection=self.database[self.collection_name]
                
                self.collection.insert_many(self.records)
                
                return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__ == '__main__':
    DATA_FILE_PATH="Network_Data\\NetworkData.csv"
    DATABASE_NAME="Network"
    COLLECTION_NAME="Cluster0"
    networkdata=NetworkDataExtract()
    records = networkdata.csv_to_json_convertor(DATA_FILE_PATH)
    inserted_record=networkdata.pushing_data_to_mongodb(records,DATABASE_NAME,COLLECTION_NAME)
    print(inserted_record)