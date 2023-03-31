import random 
from array import *
class Randomize:
    def __init__(self):
        self.__userID = [1, 2, 3, 4,5,6,7,8]
    def getRandom(self, userID):
        try:
            a = [] 
            self.__userID.remove(userID)
            for i in self.__userID:
                a.append(i)
            return random.choice(a)
        except:
            print( "Not valid UserID")
    def getMultiRandom(self, UserArray):
        try:
            a = []
            for i in UserArray:
                self.__userID.remove(i)
            for j in self.__userID:
                a.append(j)
            return random.choice(a)
        except:
            print("Not valid UserID")

runcode = Randomize()
UserArray = array('i', [1,2,3,4,5])
print(runcode.getMultiRandom(UserArray))    
