class Bottle:
    # attributes 
    brand="Aqua"
    def __init__(self,c,h,r):
        self.color=c
        self.height=h
        self.radius=r
    def printVolume(self):
        print(f"{(22/7)*(self.radius)*(self.radius)*(self.height)} mm3")
    @classmethod
    def printBrand(cls):
        print(cls.brand)
    @staticmethod
    def greet():
        print("Welcome....!")

# 4 Attr, 3 Method
# Bottle.greet()
# Bottle.printBrand() 

b1=Bottle("Black",300,30)
# b2=Bottle("Blue",500,20)

# Bottle.greet()
# b1.greet()

# b1.printVolume() #Bottle.printVolume(b1)
# b2.printVolume() #Bottle.printVolume(b2)

# b1.greet() #Bottle.greet()

# b2=Bottle()

# b1.color="Black"
# b1.brand="Aqua"

# print(b1.brand)
# print(b2.brand)

# print(Bottle.brand)

# Bottle.brand="Leo"

# print(b1.brand)
# print(b2.brand)

# b1.greet()

a=12 #int
b="Hello"
c=[1,2,3,4]

# print(type(b1)) #<class "__main__.Bottle">