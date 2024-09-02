from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline



STAGE_NAME= "Data Ingestion Stage"
try:
    logger.info(f">>>> Stage {STAGE_NAME} Started <<<<<<")
    nav = DataIngestionTrainingPipeline()
    nav.main()
    logger.info(f">>>> Stage {STAGE_NAME} Completed <<<<<\n\n X=============X")
except Exception as e:
    logger.exception(e)
    raise e