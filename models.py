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

    def __init__(self, statement, qtype,options,nextq):
        self.statement = statement
        self.qtype = qtype;
        self.options = options
        self.nextq = nextq

    def getStatement(self):
        return self.statement

    def getType(self):
        return self.qtype

    def getOptions(self):
        return self.options

    def getnextqKey(self):
        return self.nextq
        

class Product(object):
    """docstring for Product"""
    def __init__(self, arg):
        super(Product, self).__init__()
        self.arg = arg
        

yns = ["Yes","No","Sometimes"]
yna = ["Yes","No","Anything is fine"]

questions = {
    "q1": Question("Choose your price range","picker",None,"q2"),
    "q2": Question("Do you want to play games on your phone","single",yns,"q3"),
    "q3": Question("Select games you would like to play on your phone","multi",["Anything is fine","Candy Crush","Temple Run","Pokemon Go","Paper Toss"],"q4"),
    "q4": Question("Do you check emails and services like whatsapp","single",yns,"q5"),
    "q5": Question("Do you listen to music on phone?","single",yns,"q6"),
    "q6": Question("Do you watch movies on your phone?","single",yns,"q7"),
    "q7": Question("How do you watch movies","multi",["store movies on phone","online streaming as youtube"],"q8"),
    "q8": Question("Do you take photos with phone","single",yns,"q9"),
    "q9": Question("Do you use internet on your phone","single",yns,"q10"),
    "q10": Question("What apps do you use internet for","multi",["Service apps such as Ola, Uber, Zomato, Swiggy","Social network apps like twitter, fb","general web browsing","other apps"],"q11"),
    "q11": Question("Do you need more than one sim compulsorily","single",yna,"q12"),
    "q12": Question("OS Preferences","single",["Android","iOS","Anything is fine"],"q13"),
    "q13": Question("Brand Preferences","single",["Anything is fine","Apple","Samsung","LeTv","Lava","Oppo","Micromax","Canvas","Yuka"],"q14"),
    "q14": Question("Screensize","single",["Anything is fine","Small(min 4 inches)","Medium(min 4.5inches","Large(min 5inches"],"q15")
}

products = {
    
}
