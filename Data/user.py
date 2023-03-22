class User:
    def __init__(self): #indispensable
        self.__name = ""
        self.__age = 0
        self.__gender = ""
        self.__location = ""
        self.__bio = "Looking for short/long-term dating and new friends." # default value
        self.__basics = self.userBasics() #inner class
        self.__interests = self.userInterests() #inner class
        self.__account = self.userAccount() #inner class
    class userAccount: #indispensable
        def __init__(self):
            self.__username = ""
            self.__password = ""
        def setPass(self, password):
            self.__password = password
        def setUsername(self, username):
            self.__username = username
        def getPassword(self):
            return self.__password
        def getUsername(self):
            return self.__username
    class userBasics: #optional
        def __intit__(self):
            self.__height = 0
            self.__weight = 0
            self.__zodiac = ""
            self.__education = ""
            self.__workout = ""
            self.__smoke = ""
            self.__drink = ""
        def setUserBasics(self, height, weigth, zodiac, education, workout, smoke, drink):
            self.__height = height
            self.__weight = weigth
            self.__zodiac = zodiac
            self.__education = education
            self.__workout = workout
            self.__smoke = smoke
            self.__drink = drink
        def getUserBasics(self):
            return self.__height, self.__weight, self.__zodiac, self.__education, self.__workout, self.__smoke, self.__drink
    class userInterests: #optional
        def __init__(self):
            self.__sports = ""
            self.__creativity = ""
            self.__going_out = ""
            self.__staying_in = ""
            self.__film_tv = ""
            self.__reading = ""
            self.__music = ""
            self.__food = ""
            self.__traveling = ""
            self.__pets = ""
        def setUserInterests(self, sports, creativity, going_out, staying_in, film_tv, reading, music, food, traveling, pets):
            self.__sports = sports
            self.__creativity = creativity
            self.__going_out = going_out
            self.__staying_in = staying_in
            self.__film_tv = film_tv
            self.__reading = reading
            self.__music = music
            self.__food = food
            self.__traveling = traveling
            self.__pets = pets
        def getUserInterests(self):
            return self.__sports, self.__creativity, self.__going_out, self.__staying_in, self.__film_tv, self.__reading, self.__music, self.__food, self.__traveling, self.__pets
    def setName(self, name):
        self.__name = str(name)
    def setAge(self, age):    
        self.__age = int(age)
    def setGender(self, gender):
        self.__gender = str(gender)
    def setLocation(self, location):
        self.__location = str(location)
    def setBio(self, bio):    
        if bio != "None":
            self.__bio = str(bio)
    def setUserBasics(self, height, weigth, zodiac, education, workout, smoke, drink):
        self.__basics.setUserBasics(height, weigth, zodiac, education, workout, smoke, drink)
    def setUserInterests(self, sports, creativity, going_out, staying_in, film_tv, reading, music, food, traveling, pets):
        self.__interests.setUserInterests(sports, creativity, going_out, staying_in, film_tv, reading, music, food, traveling, pets)
    def getInfo(self):
        return self.__name, self.__age, self.__gender, self.__location, self.__bio
    def getUserBasics(self):
        return self.__basics.getUserBasics()
    def getUserInterests(self):
        return self.__interests.getUserInterests()
    def setUser(self, name, age, gender, location, bio, height, weight, zodiac, education, workout, smoke, drink, sports, creativity):
        self.setUserInfo(name, age, gender, location, bio)
        self.setUserBasics(height, weight, zodiac, education, workout, smoke, drink)    
        self.setUserInterests(sports, creativity)