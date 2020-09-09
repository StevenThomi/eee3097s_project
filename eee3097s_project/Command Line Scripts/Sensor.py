# general components of every sensor, unique to every sensor:
# - identification credentals
# - location of deployment
class Sensor:
    def __init__(self, sensorID, location = "33 48\' 58\" S 18 28\' 22\" E"):
        self.__sensorID = sensorID
        self.__location = location

# record sensor id
    def setSensorID(self, sensorID):
        self.__sensorID = sensorID

# record sensor location
    def setLocation(self, location):
        self.__location = location

    def getSensorID(self):
        return self.__sensorID

    def getLocation(self):
        return self.__location

# superclass output
    def __str__(self):
        return "Sensor ID: " + str(self.__sensorID) + \
                ", Location: " + self.__location
