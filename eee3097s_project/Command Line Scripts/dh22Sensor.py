# import Enum class and random number libraries
from enum import Enum, unique
from random import random

@unique
class Alert(Enum):
    NO_ALERT = 1
    HIGH_TEMPARATURE = 2
    HIGH_HUMIDITY = 3
    HIGH_TEMPARATURE_HUMIDITY = 4

# simulate the operations of a dh22sensor
# temperature and humidity are not inbuilt into the sensor
# but rather a consequence of their environment
# these variables; therefore, cannot be inbuilt into the sensor itself
class dh22Sensor(Sensor):
    def __init__(self):
        super().__init__()

# simulate the temperature in a 0°C to 70°C range - using random numbers
    def getTemperature(self):
        return (random() * 70)

# simulate the humidity in a 0% to 100% range - using random numbers
    def getHumidity(self):
        return (random() * 100)

# extract meaning from simulated measurands through alerts - defined in a
# table of alerts
    def getAlert(self, temperature, humidity):
        if(getTemperature() > 50 and getHumidity() < 30):
            return Alert(4)
        elif(getTemperature() > 50):
            return Alert(2)
        elif(getHumidity() < 30):
            return Alert(3)
        else:
            return Alert(1)

# print sensor output + dh22 sensor output
    def printSensor(self):
        temperature = getTemperature()
        humidity = getHumidity()
        alert = getAlert(temperature, humidity)

        print("DH22 Sensor: " + self.__str__() + "\tTemperature: " + \
                str(temperature) + "°C\tHumidity: " + str(humidity) + \
                "%\tAlert: " + str(alert))
