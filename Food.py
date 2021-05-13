'''
Class to describe foods
'''

import datetime

class Food:
    '''
    Constructor
    @inKey the surrogate key for the food
    @owner the owner of the food
    @name the name of the food
    @expired bool for if the food has expired
    @expDate when the food expires
    @quantity how much of the food there is
    @type how the food is inputed
    '''
    def __init__(self, inKey, inOwner, inName, inExpired, inExpDate, inQuantity, inType):
        self.surrogateKey = inKey
        self.owner = inOwner
        self.name = inName
        self.expired = inExpired
        self.expDate = inExpDate
        self.quantity = inQuantity
        self.type = inType


    #Getters and setters
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
