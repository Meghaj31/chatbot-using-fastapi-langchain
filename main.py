from fastapi import FastAPI, HTTPException, Depends, File, UploadFile
from pydantic import BaseModel
from typing import List, Annotated
import models,crud, schema
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app=FastAPI()
models.base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/user/create")
def createUser(user:schema.UserCreate, db:db_dependency):
    db_user = crud.getUser(db,userName = user.userName)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    return crud.createUser(db=db, user=user)

@app.get("/user/getbyId/{name}")
def getUserbyId(username:str,db:db_dependency):
    return crud.getUser(db,username)


@app.post("/sesison/create")
def createSession(session:schema.SessionCreate, db:db_dependency):
    return crud.createSession(db=db, session=session)
