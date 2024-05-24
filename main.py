from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app=FastAPI()
models.base.metadata.create_all(bind=engine)

class Message(BaseModel):
    messageText:str

class Sessions(BaseModel):
    sessionName:str

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
def hello():
    return "hello world"

@app.post("/message")
async def createMessage(message:Message, db:Session = Depends(get_db)):
    db_message=models.Messages(**message.model_dump())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)

@app.post("/session")
async def createSession(session:Sessions, db:Session = Depends(get_db)):
    db_session = models.Sessions(**session.model_dump())
    db.add(db_session)
    db.commit()
    db.refresh(db_session)