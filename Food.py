import datetime

class Food:
    def __init__(self, inKey, inOwner, inName, inExpired, inExpDate, inQuantity, inType):
        self.surrogateKey = inKey
        self.owner = inOwner
        self.name = inName
        self.expired = inExpired
        self.expDate = inExpDate
        self.quantity = inQuantity
        self.type = inType


    def setSurrogate(self, inKey):
        self.surrogateKey = inKey

    def getSurrogate(self):
        return self.surrogateKey

    def setOwner(self,inOwner):
        self.owner = inOwner

    def getOwner(self):
        return self.owner

    def setName(self, inName):
        self.name = inName

    def getName(self):
        return self.name

    def setExpired(self, input):
        self.expired = input

    def getExpired(self):
        return self.expired

    def setType(self, inType):
        self.type = inType

    def getType(self):
        return self.type

    def setExpDate(self, inDate):
        self.expDate = inDate

    def getExpDate(self):
        return self.expDate


    


# Create an object of type Food (with initialization values)
myFood = Food(1, "PIZZA", "Katie", True, datetime.datetime(2021, 3, 29), 10, "produce")


print(myFood.surrogateKey)

print("***************")

print(myFood.getSurrogate())



