from networksecurity.components.Data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig

import sys

if __name__=="__main__":
    try:
        tarining_pipeline_config=TrainingPipelineConfig()
        Data_Ingestion_Config=DataIngestionConfig(tarining_pipeline_config)
        Data_Ingestion=DataIngestion(Data_Ingestion_Config)
        logging.info("Starting the data ingestion component")
        dataingestionartifcate=Data_Ingestion.initiate_data_ingestion()
        print(dataingestionartifcate)
    except Exception as e:
        raise NetworkSecurityException(e,sys)