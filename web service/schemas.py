from fastapi import Form, File, UploadFile
from pydantic import BaseModel


# https://stackoverflow.com/a/60670614
class AwesomeForm(BaseModel):
    email: str
    features: int
    file: UploadFile

    @classmethod
    def as_form(
        cls,
        email: str = Form(...),
        features: int = Form(...),
        file: UploadFile = File(...)
    ):
        return cls(
            email=email,
            features=features,
            file=file
        )