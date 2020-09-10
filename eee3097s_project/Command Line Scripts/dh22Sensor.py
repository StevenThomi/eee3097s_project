# import Enum class and random number libraries, and Sensor class
from enum import Enum, unique
from random import random
from Sensor import Sensor

@unique
class Alert(Enum):
    NO_ALERT = 1
    HIGH_TEMPARATURE = 2
    HIGH_HUMIDITY = 3
    HIGH_TEMPARATURE_HUMIDITY = 4

# simulate the operations of a dh22sensor
# temperature and humidity are initialized to 0, updated
# in every fetch
class dh22Sensor(Sensor):
    def __init__(self):
        super().__init__()
        self.__temperature = 0
        self.__humidity = 0

# simulate the temperature in a 0°C to 70°C range - using random numbers
    def getTemperature(self):
        self.__temperature = random() * 70
        return self.__temperature
    
# simulate the humidity in a 0% to 100% range - using random numbers
    def getHumidity(self):
        self.__humidity = random() * 100
        return self.__humidity
    
# extract meaning from simulated measurands through alerts - defined in a
# table of alerts
    def getAlert(self):
        if(self.__temperature > 50 and self.__humidity < 30):
            return Alert(4)
        elif(self.__temperature > 50):
            return Alert(2)
        elif(self.__humidity < 30):
            return Alert(3)
        else:
            return Alert(1)

# print sensor output + dh22 sensor output
    def printSensor(self):
        temperature = getTemperature()
        humidity = getHumidity()
        # writeToDatabase()
        # write the fields to the linked database
        
        print("DH22 Sensor: " + self.__str__() + "\tTemperature: " + \
                str(temperature) + "°C\tHumidity: " + str(humidity) + \
                "%\tAlert: " + str(getAlert()))
