import logging
from src.pipeline.stage_01_data_ingestion import DataIngestiontrainingPipeline
from src.exception import CustomException
import sys
from src.pipeline.stage_02_data_validation import DataValidationTraningPipeline


STAGE_NAME = "data ingestion stage"
try:
    logging.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<<<<')
    data_ingestion = DataIngestiontrainingPipeline()
    data_ingestion.main()
    logging.info(f'>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<< \n\n x=========================x')
                    
except Exception as e :
    raise CustomException(e,sys)


STAGE_NAME = "data validation stage"
try:
    logging.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<<<<')
    data_validation=DataValidationTraningPipeline()
    data_validation.main()
    logging.info(f'>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<< \n\n x=========================x')
                    
except Exception as e :
    raise CustomException(e,sys)