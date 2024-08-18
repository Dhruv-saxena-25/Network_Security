from datetime import datetime
import os
from networksecurity.constant import training_pipeline


training_pipeline.ARTIFACT_DIR 

class TrainingPipelineConfig:
    def __init__(self, timestamp= datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name: str = training_pipeline.PIPELINE_NAME
        self.artifact_dir: str = os.path.join(training_pipeline.ARTIFACT_DIR, timestamp)
        self.timestamp: str = timestamp
class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        
        pass


class DataValidationConfig:
    def __init__(self):
        pass

class DataTransformationConfig:
    def __init__(self):
        pass


class ModelTrainerConfig:
    def __init__(self):
        pass

class ModelEvaluationConfig:
    def __init__(self):
        pass

class ModelPusherConfig:
    def __init__(self):
        pass