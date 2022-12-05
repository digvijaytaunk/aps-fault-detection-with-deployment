import os
import sys

from globs import DATA_VALIDATION_DIR_NAME, DATA_VALIDATION_REPORT_FILENAME, DATASET_FILENAME
from sensor import DATABASE_NAME, COLLECTION_NAME
from sensor.exception import SensorException
from datetime import datetime

FILE_NAME = "sensor.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"


class TrainingPipelineConfig:

    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(), "artifact", f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
        except Exception as e:
            raise SensorException(e, sys)


class DataIngestionConfig:

    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        try:
            self.database_name = DATABASE_NAME
            self.collection_name = COLLECTION_NAME
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir, "data_ingestion")
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir, "feature_store", FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir, "dataset", TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir, "dataset", TEST_FILE_NAME)
            self.test_size = 0.2
        except Exception as e:
            raise SensorException(e, sys)

    def to_dict(self, ) -> dict:
        try:
            return self.__dict__
        except Exception as e:
            raise SensorException(e, sys)


class DataValidationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_validation_dir = os.path.join(training_pipeline_config.artifact_dir, DATA_VALIDATION_DIR_NAME)
        self.report_file_path = os.path.join(self.data_validation_dir, DATA_VALIDATION_REPORT_FILENAME)
        self.missing_threshold: float = 0.2
        self.base_file_path = os.path.join(DATASET_FILENAME)


class DataTransformationConfig: ...


class ModelTrainerConfig: ...


class ModelEvaluationConfig: ...


class ModelPusherConfig: ...
