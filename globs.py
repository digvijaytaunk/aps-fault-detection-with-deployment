import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_NAME = os.getenv('DATABASE_NAME')
MONGO_DB_URL = os.getenv('MONGO_DB_URL')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')

DATA_FILE_PATH = 'dataset/aps_failure_training_set1.csv'

DATASET_FILENAME = 'aps_failure_training_set1.csv'

# Data Ingestion
FILE_NAME = "sensor.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

# Data validation
DATA_VALIDATION_DIR_NAME = 'data_validation'
DATA_VALIDATION_REPORT_FILENAME = 'report.yaml'

# Data Transformation
TARGET_COLUMN = 'class'
TRANSFORMER_OBJECT_FILE_NAME = "transformer.pkl"
TARGET_ENCODER_OBJECT_FILE_NAME = "target_encoder.pkl"
MODEL_FILE_NAME = "model.pkl"
