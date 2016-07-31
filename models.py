from sqlalchemy import Column, Integer, String
from database import Base

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    description = Column(String(2000))

    def __init__(self, description=None):
        self.description = description

    def __repr__(self):
        return '<User %r>' % (self.description)

class Product(Base):
	__tablename__ = 'products'
	id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    description = Column(String(120))
