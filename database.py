import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.file

student_collection = database.get_collection("file_collection")

def file_helper(file) -> dict:
    return {
        "id": str(file["_id"]),
        "filename": file["filename"],
        "filecontent": file["filecontent"]
    }

async def add_file(file_data: dict) -> dict:
    file = await student_collection.insert_one(file_data)
    new_file = await student_collection.find_one({"_id": file.inserted_id})
    return file_helper(new_file)