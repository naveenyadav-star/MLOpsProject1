from mlProject.config.configuration import  ConfigurationManager
from mlProject.components.data_model_evaluation import ModelEvaluation
from mlProject import logger


STAGE_NAME= "Data Model Evaluation Stage"



class DataModelEvaluationPipeline:
    def __init__(self) -> None:
        pass
        
        
    def main(self):

        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.log_into_mlflow()
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    try:
        logger.info(f">>>> Stage {STAGE_NAME} Started <<<<<<")
        nav =  DataModelEvaluationPipeline()
        nav.main()
        logger.info(f">>>> Stage {STAGE_NAME} Completed <<<<<\n\n X=============X")
    except Exception as e:
        logger.exception(e)
        raise e