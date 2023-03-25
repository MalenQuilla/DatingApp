class User:
    def __init__(self): #indispensable
        self.__name = ""
        self.__age = 0
        self.__gender = ""
        self.__location = ""
        self.__bio = "Looking for short/long-term dating and new friends." # default value
        self.__basics = self.userBasics() #inner class
        self.__interests = self.userInterests() #inner class
        self.__account = self.userAccount() #inner classz
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
    #basics
    def setHeight(self, height, weigth, zodiac, education, workout, smoke, drink):
        self.__height.setHeight(height)
    def setWeight(self, weight):
        self.__weight.setWeight(weight)
    def setZodiac(self, zodiac):
        self.__zodiac.setZodiac(zodiac)
    def setEducation(self, education):
        self.__education.setEducation(education)
    def setWorkout(self, workout):
        self.__workout.setWorkout(workout)
    def setSmoke(self, smoke):
        self.__smoke.setSmoke(smoke)
    def setDrink(self, drink):
        self.__drink.setDrink(drink)
    #interests
    def setSports(self, sports):
        self.__sports.setSports(sports)
    def setCreativity(self, creativity):
        self.__creativity.setCreativity(creativity)
    def setGoing_out(self, going_out):
        self.__going.setGoing_out(going_out)
    def setStaying_in(self, staying_in):
        self.__staying_in.setStaying_in(staying_in)
    def setFilm_tv(self, film_tv):
        self.__film_tv.setFilm_tv(film_tv)
    def setReading(self, reading):
        self.__reading.setReading(reading)
    def setMusic(self, music):
        self.__music.setMusic(music)
    def setFood(self, food):
        self.__food.setFood(food)
    def setTraveling(self, traveling):
        self.__traveling.setTraveling(traveling)
    def setPets(self, pets):
        self.__pets.setPets(pets)
    def getInfo(self):
        return self.__name, self.__age, self.__gender, self.__location, self.__bio
    def getUserBasics(self):
        return self.__height.setHeight(), self.__weight.setWeight(), self.__zodiac.setZodiac(), self.__education.setEducation(), self.__workout.setWorkout(), self.__smoke.setSmoke(), self.__drink.setDrink()
    def getUserInterests(self):
        return self.__sports.setSports(), self.__creativity.setCreativity(), self.__going.setGoing_out(), self.__staying_in.setStaying_in(), self.__film_tv.setFilm_tv(), self.__reading.setReading(), self.__music.setMusic(), self.__food.setFood(), self.__traveling.setTraveling()
    def setUser(self, name, age, gender, location, bio, height, weight, zodiac, education, workout, smoke, drink, sports, creativity):
        self.setUserInfo(name, age, gender, location, bio)
        self.setUserBasics(height, weight, zodiac, education, workout, smoke, drink)    
        self.setUserInterests(sports, creativity)