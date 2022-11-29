import os

from dotenv import load_dotenv

print(f"Loading environment variable from .env file")

load_dotenv()

MONGO_CONNECTION_STRING = os.getenv('MONGO_CONNECTION_STRING')
COLLECTION_NAME: str = os.getenv("COLLECTION_NAME")
DATABASE_NAME: str = os.getenv("DATABASE_NAME")

aws_access_key_id: str = os.getenv("AWS_ACCESS_KEY_ID")
aws_access_secret_key: str = os.getenv("AWS_SECRET_ACCESS_KEY")
