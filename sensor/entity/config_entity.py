import os
import sys

from globs import DATA_VALIDATION_DIR_NAME, DATA_VALIDATION_REPORT_FILENAME, DATASET_FILENAME, \
    TRANSFORMER_OBJECT_FILE_NAME, TARGET_ENCODER_OBJECT_FILE_NAME, FILE_NAME, TRAIN_FILE_NAME, TEST_FILE_NAME, \
    MODEL_FILE_NAME
from sensor import DATABASE_NAME, COLLECTION_NAME
from sensor.exception import SensorException
from datetime import datetime


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
            # TODO remove dataset dir level
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


class DataTransformationConfig:

    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_transformation_dir = os.path.join(training_pipeline_config.artifact_dir, "data_transformation")
        self.transform_object_path = os.path.join(self.data_transformation_dir, "transformer",
                                                  TRANSFORMER_OBJECT_FILE_NAME)
        self.transformed_train_path = os.path.join(self.data_transformation_dir, "transformed",
                                                   TRAIN_FILE_NAME.replace("csv", "npz"))
        self.transformed_test_path = os.path.join(self.data_transformation_dir, "transformed",
                                                  TEST_FILE_NAME.replace("csv", "npz"))
        self.target_encoder_path = os.path.join(self.data_transformation_dir, "target_encoder",
                                                TARGET_ENCODER_OBJECT_FILE_NAME)


class ModelTrainerConfig:

    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.model_trainer_dir = os.path.join(training_pipeline_config.artifact_dir, "model_trainer")
        self.model_path = os.path.join(self.model_trainer_dir, "model", MODEL_FILE_NAME)
        self.expected_score = 0.7
        self.overfitting_threshold = 0.1


class ModelEvaluationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.change_threshold = 0.01


class ModelPusherConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.model_pusher_dir = os.path.join(training_pipeline_config.artifact_dir, "model_pusher")
        self.saved_model_dir = os.path.join("saved_models")
        self.pusher_model_dir = os.path.join(self.model_pusher_dir, "saved_models")
        self.pusher_model_path = os.path.join(self.pusher_model_dir, MODEL_FILE_NAME)
        self.pusher_transformer_path = os.path.join(self.pusher_model_dir, TRANSFORMER_OBJECT_FILE_NAME)
        self.pusher_target_encoder_path = os.path.join(self.pusher_model_dir, TARGET_ENCODER_OBJECT_FILE_NAME)
