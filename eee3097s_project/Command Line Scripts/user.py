from random import randint

class User:
    def __init__(self, name, phone, password, loginStatus = "True"):
        self.__userID = randint(0,1000)
        self.__name = name
        self.__phone = phone
        self.__password = password
        self.__loginStatus = loginStatus

    def setUserID(self):
        self.__userID = randint(0,1000)

    def setName(self, name):
        self.__name = name

    def setPhone(self, phone):
        self.__phone = phone

    def setPassword(self, password):
        self.__password = password

    def setLoginStatus(self):
        self.__loginStatus = (not self.__loginStatus)

    def getUserID(self):
        return self.__userID

    def getName(self, name):
        return self.__name

    def getPhone(self, phone):
        return self.__phone

    def getPassword(self, password):
        return self.__password

    def getLoginStatus(self):
        return self.__loginStatus

    def __str__(self):
        return "UserID: " + self.__userID + ", Name: " + self.__name + \
                ", Phone: " + self.__phone + ", Password: " + \
                self.__password + ", Login Status: " + self.__loginStatus
