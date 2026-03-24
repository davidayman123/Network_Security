from networksecurity.components.Data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig

import sys

if __name__=="__main__":
    try:
        tarining_pipeline_config=TrainingPipelineConfig()
        Data_Ingestion_Config=DataIngestionConfig(tarining_pipeline_config)
        Data_Ingestion=DataIngestion(Data_Ingestion_Config)
        logging.info("Starting the data ingestion component")
        dataingestionartifcate=Data_Ingestion.initiate_data_ingestion()
        logging.info("Data ingestion component completed")
        print(dataingestionartifcate)
        data_validation_config=DataValidationConfig(tarining_pipeline_config)
        data_validation=DataValidation(data_validation_config,dataingestionartifcate)
        logging.info("Starting the data validation component")
        data_validation_artifacte=data_validation.initiate_data_validation()
        logging.info("Data validation component completed")
        print(data_validation_artifacte)
        data_transformation_config=DataTransformationConfig(tarining_pipeline_config)
        logging.info("Starting the data transformation component")
        data_transformation=DataTransformation(data_validation_artifacte,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        logging.info("Data transformation component completed")
        print(data_transformation_artifact)
        logging.info("Starting the model trainer component")
        model_trainer_config=ModelTrainerConfig(tarining_pipeline_config)
        model_trainer=ModelTrainer(model_trainer_config,data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()
        logging.info("Model trainer component completed")
    except Exception as e:
        raise NetworkSecurityException(e,sys)