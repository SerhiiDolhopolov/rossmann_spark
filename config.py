import os

from dotenv import load_dotenv

load_dotenv()

S3_HOST = os.getenv("S3_HOST", "localhost")
S3_PORT = os.getenv("S3_PORT", 9000)
S3_ENDPOINT = f"{S3_HOST}:{S3_PORT}"
S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")