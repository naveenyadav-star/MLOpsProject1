from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validations import DataValidationPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationPipeline
from mlProject.pipeline.stage_04_data_model_train import DataModelTrainPipeline
from mlProject.pipeline.stage_05_data_evaluation import DataModelEvaluationPipeline



STAGE_NAME= "Data Ingestion Stage"
try:
    logger.info(f">>>> Stage {STAGE_NAME} Started <<<<<<")
    nav = DataIngestionTrainingPipeline()
    nav.main()
    logger.info(f">>>> Stage {STAGE_NAME} Completed <<<<<\n\n X=============X")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>> Stage {STAGE_NAME} Started <<<<<<")
    data_validation= DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>> Stage {STAGE_NAME} Completed <<<<<\n\n X=============X")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>> Stage {STAGE_NAME} Started <<<<<<")
    data_validation= DataTransformationPipeline()
    data_validation.main()
    logger.info(f">>>> Stage {STAGE_NAME} Completed <<<<<\n\n X=============X")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Model Trainer Stage"
try:
    logger.info(f">>>> Stage {STAGE_NAME} Started <<<<<<")
    data_validation= DataModelTrainPipeline()
    data_validation.main()
    logger.info(f">>>> Stage {STAGE_NAME} Completed <<<<<\n\n X=============X")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME= "Data Model Evaluation Stage"
try:
    logger.info(f">>>> Stage {STAGE_NAME} Started <<<<<<")
    nav =  DataModelEvaluationPipeline()
    nav.main()
    logger.info(f">>>> Stage {STAGE_NAME} Completed <<<<<\n\n X=============X")
except Exception as e:
    logger.exception(e)
    raise e