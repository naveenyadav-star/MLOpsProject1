from mlProject.components.data_transformation import DataTransformation
from mlProject.config.configuration import ConfigurationManager
from mlProject import logger

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline():
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.train_test_spliting()
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    try:
        logger.info(f">>>> Stage {STAGE_NAME} Started <<<<<<")
        data_validation= DataTransformationPipeline()
        data_validation.main()
        logger.info(f">>>> Stage {STAGE_NAME} Completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e