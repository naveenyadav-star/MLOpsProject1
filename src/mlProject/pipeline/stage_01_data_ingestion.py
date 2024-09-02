from mlProject.config.configuration import  ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logger


STAGE_NAME= "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    try:
        logger.info(f">>>> Stage {STAGE_NAME} Started <<<<<<")
        nav = DataIngestionTrainingPipeline()
        nav.main()
        logger.info(f">>>> Stage {STAGE_NAME} Completed <<<<<\n\n X=============X")
    except Exception as e:
        logger.exception(e)
        raise e