from sqlalchemy import Column, Integer, String
from database import Base
import random

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

########################### QUESTIONS ######################################


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
        

yns = ["Yes","No","Sometimes"]
yna = ["Yes","No","Anything is fine"]

single = "single"
multi = "multi"
picker = "picker"

questions = {
    "q1": Question("Choose your price range",picker,None,"q2"),
    "q2": Question("Do you want to play games on your phone",single,yns,"q3"),
    "q3": Question("Select games you would like to play on your phone",multi,["Anything is fine","Candy Crush","Temple Run","Pokemon Go","Paper Toss"],"q4"),
    "q4": Question("Do you check emails and services like whatsapp",single,yns,"q5"),
    "q5": Question("Do you listen to music on phone?",single,yns,"q6"),
    "q6": Question("How do you usually listen music",multi,["FM Radio,youtube,music streaming apps like saavn,songs on my mobile"],"q7"),
    "q7": Question("Do you watch movies on your phone?",single,yns,"q8"),
    "q8": Question("How do you watch movies",multi,["store movies on phone","online streaming as youtube"],"q9"),
    "q9": Question("Do you take photos with phone",single,yns,"q10"),
    "q10": Question("Do you use internet on your phone",single,yns,"q11"),
    "q11": Question("What apps do you use internet for",multi,["Service apps such as Ola, Uber, Zomato, Swiggy","Social network apps like twitter, fb","general web browsing","other apps"],"q12"),
    "q12": Question("Do you need more than one sim compulsorily",single,yna,"q13"),
    "q13": Question("OS Preferences",single,["Android","iOS","Anything is fine"],"q14"),
    "q14": Question("Brand Preferences",single,["Anything is fine","Apple","Samsung","LeTv","Lava","Oppo","Micromax","Canvas","Yuka"],"q15"),
    "q15": Question("Screensize",single,["Anything is fine","Small(min 4 inches)","Medium(min 4.5inches","Large(min 5inches"],None)
}  

class Product(object):
    """docstring for Product"""
    def __init__(self, arg):
        super(Product, self).__init__()
        self.arg = arg

    def __init__(self,pid,os,brand,name,price,ram,battery,screenRes,pType,sims,sCamRes,pCamRes,cores):
        self.pid = pid
        self.os = os
        self.brand = brand
        self.name = name
        self.price = price
        self.ram = ram
        self.battery = battery
        self.screenRes = screenRes
        self.pType = pType # phone type
        self.sims = sims # number of sims
        self.sCamRes = sCamRes
        self.pCamRes = pCamRes
        self.cores = cores


########################### QUESTIONS ######################################



########################### PRODUCTS ######################################

android = "Android"
ios = "iOS"
windows = "windows"
os = [android,ios,windows]

samsung = "Samsung"
xolo = "xolo"
moto = "Motorola"
leeco = "LeEco"
apple = "Apple"
asus = "Asus"
honor = "Honor"
intex = "Intex"
infocus = "In Focus"
mi = "Mi"
lava = "Lava"
nokia = "Nokia"

brandsDict = {
    android:[samsung,xolo,moto,leeco,asus,honor,intex,infocus,mi,lava],
    ios:[apple],
    windows:[samsung,moto,asus,nokia]
}

## Generate products information
# getr denotes get Random
# gen denotes generate
# (pid,os,brand,name,price,ram,battery,screenRes,pType,sims,sCamRes,pCamRes,cores):

def genRand(num):
    products = {}
    for i in range(0,num):
        pid = i
        # os = getrOS() # get random OS
        # brand = getrBrand(os) 
        # name = genName(os,brand)
        price = getrPrice()
        ram = getrRam() # in GB
        battery = getrBattery() # in mAH
        screenRes = getrRes()
        pType = "Smart"
        sims = getrSims() # number of sims
        sCamRes = getrsCamRes()
        pCamRes = getrpCamRes()
        cores = getrCores()

        #generate and add to products list
        products.append(Product(pid,os,brand,name,price,ram,battery,screenRes,pType,sims,sCamRes,pCamRes,cores))
    return products

def getrOS():
    return random.choice(os)

def getrBrand(os):
    brands = brandsDict[os]
    return random.choice(brands)

tackyNames = ["Aqua","Baba","Chacha","Dadi","Eel","Filmy","Eco","Gandu","Halwa","Insaan","Jacky","Khan"]
def genName(os,brand):
    return random.choice(tackyNames)

def getrPrice():
    return random.randint(6000,80000)


def getrRam():
    return random.randint(2,12)/2 #1,6 are inclusive

def getrBattery():
    return random.randint(100,500)*10

resTypes = ["HD","HD+","HQVGA","HVGA","nHD","Quad HD"]
def getrRes():
    return random.choice(resTypes)

def getrSims():
    return random.randint(1,4)

def getrsScamRes(): #gives float between 2 and 8 MP
    return random.randint(20,80)/10

def getrpCamRes():#gives float between 4 and 16 MP
    return random.randint(40,160)/10

def getrCores():
    return random.choice([1,2,4])

products = genRand(100);


########################### PRODUCTS ######################################

