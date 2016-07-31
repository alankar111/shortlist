from sqlalchemy import Column, Integer, String
from database import Base

# class Question(Base):
#     __tablename__ = 'questions'
#     id = Column(Integer, primary_key=True)
#     description = Column(String(2000))

#     def __init__(self, description=None):
#         self.description = description

#     def __repr__(self):
#         return '<User %r>' % (self.description)

# class Product(Base):
# 	__tablename__ = 'products'
# 	id = Column(Integer, primary_key=True)
#     name = Column(String(50), unique=True)
#     description = Column(String(120))

class Question(object):
    """docstring for Question"""
    def __init__(self, arg):
        super(Question, self).__init__()
        self.arg = arg

    def __init__(self, statement, qtype,options):
        self.statement = statement
        self.qtype = qtype;
        self.options = options
        


        

questions = {
    "q1": Question("Choose your price range","picker",None)
    "q2": Question("Do you want to play games on your phone","single",["Yes","No","Maybe"])
    "q3": Question("Select games you would like to play on your phone","multi",["Anything is fine","Candy Crush","Temple Run","Pokemon Go","Paper Toss"])

}

products = {
    
}
