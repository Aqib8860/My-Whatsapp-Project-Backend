import os
from dotenv import load_dotenv

load_dotenv()

ALLOWED_HOST = ["localhost", "127.0.0.1", "13.235.91.255", "ec2-13-235-91-255.ap-south-1.compute.amazonaws.com"]

MONGODB_URL = os.environ.get("MONGODB_URL")
DB_NAME = os.environ.get("DB_NAME")
TestVar = "Test variable"