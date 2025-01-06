import os
import databases
import sqlalchemy
from dotenv import load_dotenv

load_dotenv()


DATABASE_URL = os.environ.get("DATABASE_URL")

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

