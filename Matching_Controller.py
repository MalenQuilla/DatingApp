class Match:
    def __init__(self):
        self.__like = {}
        self.__info = {}
    def setInfo(self, name, id):
        self.__info.update({name : id})
    def getInfo(self):
        return self.__info
    def like(self, name, id, likedName, likedId):
        print(str(name) + "liked" + str(likedName))
        self.__like.update({id : likedId})
    def getLike(self):
        return self.__like
    def swapInDict(self, a):
        new_dict = {
            value: key for key, value in a.items()
        }
        return new_dict
    def checkForMatch(self):
        new_dict = self.swapInDict(self.__like)
        common_likes = dict()
        for key in self.__like:
            if (key in new_dict and self.__like[key] == new_dict[key]):
                common_likes[key] = self.__like[key]
        return common_likes


runcode = Match()

runcode.setInfo("Thang", "12")
runcode.setInfo("TramAnh", "13")
runcode.setInfo("TUng", "14")
runcode.setInfo("Linh", "15")
print(runcode.getInfo())
runcode.like("Thang", "12", "TramAnh", "13")
runcode.like("TramAnh", "13", "Thang", "12")
runcode.getLike()
print(runcode.checkForMatch())
