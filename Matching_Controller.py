import random
from database_controller import show_seen, counts, update_seen

class Randomize:
    def __init__(self, user_id):
        count = counts()
        array = []
        for i in range(count):
            array.append(str(i + 1))
        self.__IdArray = array
        self.__user_id = user_id
        
        seens = show_seen()
        seen = seens[user_id - 1]
        self.__seenArray = seen[0].split(" ")
    def returnInfo(self):
        return self.__IdArray, self.__seenArray
    def getMultiRandom(self):
        a = []
        for i in self.__seenArray:
            try:
                self.__IdArray.remove(i)
            except ValueError:
                pass
        for j in self.__IdArray:
            a.append(j)
        
        if len(a) == 0:
            return self.__user_id    
        
        print(a)
        x = random.choice(a)
        self.__seenArray.append(x)
        update_seen((' '.join([str(elem) for elem in self.__seenArray])), self.__user_id)
        return x