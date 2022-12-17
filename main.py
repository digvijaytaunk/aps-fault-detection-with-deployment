from globs import INPUT_FILE_PATH_TO_PREDICT
from sensor.pipeline.batch_prediction import start_batch_prediction
from sensor.pipeline.training_pipeline import start_training_pipeline

if __name__ == "__main__":
    try:
        # start_training_pipeline()
        output_file = start_batch_prediction(input_file_path=INPUT_FILE_PATH_TO_PREDICT)
        print(output_file)
    except Exception as e:
        print(e)
