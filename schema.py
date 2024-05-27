from pydantic import BaseModel

class UserCreate(BaseModel):
    userName:str

class SessionCreate(BaseModel):
    user_id: int

class QueryCreate(BaseModel):
    session_id: int
    query_text: str

class DocumentUpload(BaseModel):
    fliename:str
    content:str