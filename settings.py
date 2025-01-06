import os
from dotenv import load_dotenv

load_dotenv()

ALLOWED_HOST = ["localhost", "127.0.0.1"]

MONGODB_URL = os.environ.get("MONGODB_URL")
DB_NAME = os.environ.get("DB_NAME")
TestVar = "Test variable"