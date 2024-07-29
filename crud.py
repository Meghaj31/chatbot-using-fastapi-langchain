from sqlalchemy.orm import Session
import models, schema

def getUser(db:Session, userName:str):
    return db.query(models.User).filter(models.User.userName == userName).first()

def createUser(db:Session, user:schema.UserCreate):
    db_user = models.User(userName=user.userName)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def createSession(db:Session, session:schema.SessionCreate):
    db_sesion = models.Session(user_id=session.user_id)
    db.add(db_sesion)
    db.commit()
    db.refresh(db_sesion)
    return db_sesion