from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


## configuration of the Data Ingestion Config

from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact
import os
import sys
import numpy as np
import pandas as pd
import pymongo
import certifi
from typing import List
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv
from pymongo.errors import ServerSelectionTimeoutError
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
FALLBACK_CSV_PATH=os.getenv("DATA_INGESTION_FALLBACK_CSV", os.path.join("Network_Data", "phisingData.csv"))


class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def _load_local_backup_dataframe(self) -> pd.DataFrame:
        """Load a local CSV when MongoDB is unavailable."""
        try:
            if not os.path.exists(FALLBACK_CSV_PATH):
                raise FileNotFoundError(
                    f"Fallback dataset not found at: {FALLBACK_CSV_PATH}. "
                    "Set DATA_INGESTION_FALLBACK_CSV to a valid CSV path."
                )

            logging.info(f"Loading fallback dataset from local path: {FALLBACK_CSV_PATH}")
            df = pd.read_csv(FALLBACK_CSV_PATH)
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            df.replace({"na": np.nan}, inplace=True)
            print("Shape of fallback dataset", df.shape)
            return df
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def _get_mongo_client(self) -> pymongo.MongoClient:
        """Create a Mongo client with explicit CA certs for Atlas TLS handshakes."""
        try:
            if not MONGO_DB_URL:
                raise ValueError("MONGO_DB_URL is not set. Add it to your environment or .env file.")

            client = pymongo.MongoClient(
                MONGO_DB_URL,
                tls=True,
                tlsCAFile=certifi.where(),
                serverSelectionTimeoutMS=30000,
                retryWrites=True,
            )
            client.admin.command("ping")
            return client
        except ServerSelectionTimeoutError:
            raise
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def export_collection_as_dataframe(self):
        """
        Read data from mongodb
        """
        try:
            database_name=self.data_ingestion_config.database_name
            collection_name=self.data_ingestion_config.collection_name
            self.mongo_client=self._get_mongo_client()
            collection=self.mongo_client[database_name][collection_name]

            df=pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df=df.drop(columns=["_id"],axis=1)
            print("Shape of original dataset",df.shape)
            df.replace({"na":np.nan},inplace=True)
            return df
        except ServerSelectionTimeoutError as e:
            logging.warning(
                "MongoDB TLS handshake failed. Falling back to local dataset. "
                f"Original error: {e}"
            )
            return self._load_local_backup_dataframe()
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def export_data_into_feature_store(self,dataframe: pd.DataFrame):
        try:
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path
            #creating folder
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def split_data_as_train_test(self,dataframe: pd.DataFrame):
        try:
            train_set, test_set = train_test_split(
                dataframe, test_size=self.data_ingestion_config.train_test_split_ratio
            )
            logging.info("Performed train test split on the dataframe")

            logging.info(
                "Exited split_data_as_train_test method of Data_Ingestion class"
            )
            
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            
            os.makedirs(dir_path, exist_ok=True)
            
            logging.info(f"Exporting train and test file path.")
            
            train_set.to_csv(
                self.data_ingestion_config.training_file_path, index=False, header=True
            )

            test_set.to_csv(
                self.data_ingestion_config.testing_file_path, index=False, header=True
            )
            logging.info(f"Exported train and test file path.")

            
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
        
    def initiate_data_ingestion(self):
        try:
            dataframe=self.export_collection_as_dataframe()
            dataframe=self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)
            dataingestionartifact=DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
                                                        test_file_path=self.data_ingestion_config.testing_file_path)
            return dataingestionartifact

        except Exception as e:
            raise NetworkSecurityException(e,sys)