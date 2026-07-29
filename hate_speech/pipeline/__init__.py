import sys
from hate_speech.logger import logging
from hate_speech.exception import CustomException
from hate_speech.entity.config_entity import DataIngestionConfig
from hate_speech.entity.artifact_entity import DataIngestionArtifacts
from hate_speech.components.data_ingestion import DataIngestion


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()

    def start_data_ingestion(self)->DataIngestionArtifacts:
     logging.info("Entered the start_data_ingestion method of TrainingPipeline class")
     try:
        logging.info("Getting the data from GCloud storage bucket")
        data_ingestion=DataIngestion(data_ingestion_config=self.data_ingestion_config)
        data_ingestion_artifacts=data_ingestion.initiate_data_ingestion()

        logging.info("Got the train and valid from GCLoud Storage")
        logging.info("Exited the satrt_data_ingestion and method of TrainPipeline class")
     except Exception as e:
        raise CustomException(e,sys) from e

    def run_pipeline(self) -> None:
        logging.info("entered the run_pipeline method of TrainPipeline class")
        try:
            data_ingestion_artifacts=self.start_data_ingestion()

            logging.info("Exited the run_pipeline method of TrainPipeline class")
        
        except Exception as e:
            raise CustomException(e,sys) from e

    