import logging
from src.pipeline.stage_01_data_ingestion import DataIngestiontrainingPipeline
from src.exception import CustomException
import sys


STAGE_NAME = "data ingestion stage"
try:
    logging.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<<<<')
    obj = DataIngestiontrainingPipeline()
    obj.main()
    logging.info(f'>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<< \n\n x=========================x')
                    
except Exception as e :
    raise CustomException(e,sys)