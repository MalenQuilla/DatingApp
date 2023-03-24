class User:
    def __init__(self): #indispensable
        self.__name = ""
        self.__age = 0
        self.__gender = ""
        self.__location = ""
        self.__bio = "Looking for short/long-term dating and new friends." # default value
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

    #user interest
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
    #basics
    def setHeight(self, height):
        self.__height = height
    def setWeight(self, weight):
        self.__weight = weight
    def setZodiac(self, zodiac):
        self.__zodiac = zodiac
    def setEducation(self, education):
        self.__education = education
    def setWorkout(self, workout):
        self.__workout = workout
    def setSmoke(self, smoke):
        self.__smoke = smoke
    def setDrink(self, drink):
        self.__drink = drink
    #interests
    def setSports(self, sports):
        self.__sports = sports
    def setCreativity(self, creativity):
        self.__creativity = creativity
    def setGoing_out(self, going_out):
        self.__going_out = going_out
    def setStaying_in(self, staying_in):
        self.__staying_in = staying_in
    def setFilm_tv(self, film_tv):
        self.__film_tv = film_tv
    def setReading(self, reading):
        self.__reading = reading
    def setMusic(self, music):
        self.__music = music
    def setFood(self, food):
        self.__food = food
    def setTraveling(self, traveling):
        self.__traveling = traveling
    def setPets(self, pets):
        self.__pets = pets
    def getInfo(self):
        return self.__name, self.__age, self.__gender, self.__location, self.__bio
    def getUserBasics(self):
        return self.__height, self.__weight, self.__zodiac, self.__education, self.__workout, self.__smoke, self.__drink
    def getUserInterests(self):
        return self.__sports, self.__creativity, self.__going_out, self.__staying_in, self.__film_tv, self.__reading, self.__music, self.__food, self.__traveling
    def setUser(self, name, age, gender, location, bio, height, weight, zodiac, education, workout, smoke, drink, sports, creativity):
        self.setUserInfo(name, age, gender, location, bio)
        self.setUserBasics(height, weight, zodiac, education, workout, smoke, drink)    
        self.setUserInterests(sports, creativity)