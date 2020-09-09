# import random number library
from random import randint

# general traits of officials responsible for monitoring the sensor
# system
class User:
    def __init__(self, name, phone, password = "0000", loginStatus = "True"):
        self.__userID = randint(0,1000)
        self.__name = name
        self.__phone = phone
        self.__password = password
        self.__loginStatus = loginStatus

# unique user identifier - set by system
    def setUserID(self):
        self.__userID = randint(0,1000)

    def setName(self, name):
        self.__name = name

    def setPhone(self, phone):
        self.__phone = phone

# user password - login required
    def setPassword(self, password):
        self.__password = password

# login status toggles between logged in and logged out
    def setLoginStatus(self):
        self.__loginStatus = (not self.__loginStatus)

    def getUserID(self):
        return self.__userID

    def getName(self):
        return self.__name

    def getPhone(self):
        return self.__phone

    def getPassword(self):
        return self.__password

    def getLoginStatus(self):
        return self.__loginStatus

# display user attributes
    def __str__(self):
        return "UserID: " + str(self.__userID) + ", Name: " + self.__name + \
                ", Phone: " + self.__phone + ", Password: " + \
                self.__password + ", Login Status: " + str(self.__loginStatus)
