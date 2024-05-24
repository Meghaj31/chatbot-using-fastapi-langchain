from sqlalchemy import Boolean, Column, ForeignKey, Integer, String 
from database import base

class Sessions(base):
    __tablename__ = 'Sessions'

    id=Column(Integer, primary_key=True, index=True)
    sessionName = Column(String)

class Messages(base):
    __tablename__ = 'Messages'
    id = Column(Integer, primary_key=True, index=True)
    messageText=Column(String)
    sessionId = Column(Integer, ForeignKey("Sessions.id"))