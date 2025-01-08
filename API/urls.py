import requests
import settings

# from bson import ObjectId

from dotenv import load_dotenv

from datetime import datetime, date

from motor.motor_asyncio import AsyncIOMotorClient

from typing import Optional, Dict
from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from .models import User
from . import views



load_dotenv()

# Mongodb Settings
mongo_db_url = settings.MONGODB_URL

client = AsyncIOMotorClient(mongo_db_url)
db = client.get_database(settings.DB_NAME)

# Url router
api_router = APIRouter()


@api_router.get("/")
async def read_root():
    return {"message": "permission denied"}

# User Registration
@api_router.post("/register/")
async def register(
    form_data: User
):
    return await views.register_user_view(db, form_data)


@api_router.get("/users/")
async def get_users_list():
    return await views.get_users_view(db)
