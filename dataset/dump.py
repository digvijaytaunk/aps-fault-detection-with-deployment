import json

from sensor import DATABASE_NAME, COLLECTION_NAME
from sensor.mongo_db import mongo_client

db = mongo_client.get_database(DATABASE_NAME)
col = db.get_collection(COLLECTION_NAME)


if __name__ == '__main__':
    import pandas as pd
    df = pd.read_csv('aps_failure_training_set1.csv')
    df.reset_index(drop=True, inplace=True)
    json_record = list(json.loads(df.T.to_json()).values())
    col.insert_many(json_record)

