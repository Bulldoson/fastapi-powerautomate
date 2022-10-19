from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class FileSchema(BaseModel):
    filename: str = Field(...)
    filecontent: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "filename": "file",
                "filecontent": "eztjkZEKdkslezKzlsdKDSEL",
            }
        }


class UpdateStudentModel(BaseModel):
    filename: Optional[str]
    filecontent: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "filename": "file",
                "filecontent": "eztjkZEKdkslezKzlsdKDSEL",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}