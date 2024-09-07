
from mlProject.components.data_validations import DataValiadtion
from mlProject.config.configuration import ConfigurationManager
from mlProject import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationPipeline():
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValiadtion(config=data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            raise e


if __name__ == '__main__':
    try:
        logger.info(f">>>> Stage {STAGE_NAME} Started <<<<<<")
        data_validation= DataValidationPipeline()
        data_validation.main()
        logger.info(f">>>> Stage {STAGE_NAME} Started <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

        