from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import base

class User(base):
    __tablename__ = 'users'

    id=Column(Integer, primary_key=True, index=True)
    userName = Column(String, unique=True, index=True)
    sessions = relationship("Session", back_populates="user")

class Session(base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime)
    user = relationship("User", back_populates="sessions")
    queries = relationship("Query", back_populates="session")

class Document(base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    document_name = Column(String)
    document_content = Column(String)

class Query(base):
    __tablename__  = "queries"
    id = Column(Integer, primary_key=True,index=True)
    query_text = Column(String)
    session_id = Column(Integer, ForeignKey('sessions.id'))
    query_response = Column(String)
    created_at = Column(DateTime)
    session = relationship("Session", back_populates="queries")

