from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_model_train import ModelTrainer
from mlProject import logger


STAGE_NAME = "Data Model Trainer Stage"

class DataModelTrainPipeline():
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    try:
        logger.info(f">>>> Stage {STAGE_NAME} Started <<<<<<")
        data_validation= DataModelTrainPipeline()
        data_validation.main()
        logger.info(f">>>> Stage {STAGE_NAME} Completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e