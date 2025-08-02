# app/models/sqlalchemy_task.py

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    completed = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}', completed={self.completed})>"