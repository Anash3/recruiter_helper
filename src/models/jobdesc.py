from pydantic import BaseModel

class JobDescriptionResponse(BaseModel):
    job_description: str
