import json
from fastapi.responses import JSONResponse


def serialize_mongo_document(doc):
    """ Helper function to convert MongoDB document ObjectId to string """
    if "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return doc


async def register_user_view(db, form_data):
    try:
        users_db = db.get_collection('users')
        data = form_data.dict()
        
        is_exists = await users_db.find_one({"email": data.get("email")})
        if is_exists:
            return JSONResponse({"error": "Email already exists"}, status_code=400)
        
        new_user = await users_db.insert_one(data)
        user = await users_db.find_one({"_id": new_user.inserted_id})

        user["_id"] = str(user["_id"])
        user["generated_on"] = str(user["generated_on"])
        
        return JSONResponse({"message": "User Successfully Registered", "user": user})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


async def get_users_view(db):
    users = await db.get_collection('users').find().to_list(length=None)
    # data = [serialize_mongo_document(doc) for doc in users]
    for user in users:
        user["_id"] = str(user["_id"])
        user["generated_on"] = str(user["generated_on"])


    return JSONResponse(users)



