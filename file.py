from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from database import (
    add_file,
)
from models.file import (
    ErrorResponseModel,
    ResponseModel,
    FileSchema,
    UpdateStudentModel,
)

router = APIRouter()

@router.post("/", response_description="File data added into the database")
async def add_file_data(file: FileSchema = Body(...)):
    file = jsonable_encoder(file)
    new_file = await add_file(file)
    return ResponseModel(new_file, "File added successfully.")
