import sys
import logging
from src.exception import CustomException


from src.pipeline.stage_01_data_ingestion import DataIngestiontrainingPipeline
from src.pipeline.stage_02_data_validation import DataValidationTraningPipeline
from src.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.pipeline.stage_04_model_trainer import ModeltrainerTrainingPipeline
from src.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

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


STAGE_NAME = "data transformation stage"
try:
    logging.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<<<<')
    data_transformation=DataTransformationTrainingPipeline()
    data_transformation.main()
    logging.info(f'>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<< \n\n x=========================x')
                    
except Exception as e :
    raise CustomException(e,sys)


STAGE_NAME = "model trainer stage"
try:
    logging.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<<<<')
    model_trainer= ModeltrainerTrainingPipeline()
    model_trainer.main()
    logging.info(f'>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<< \n\n x=========================x')
                    
except Exception as e :
    raise CustomException(e,sys)



STAGE_NAME = "model evaluation stage"
try:
    logging.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<<<<')
    model_evaluation= ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logging.info(f'>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<< \n\n x=========================x')
                    
except Exception as e :
    raise CustomException(e,sys)