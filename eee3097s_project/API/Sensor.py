# Sensor class
class Sensor:
    def __init__(self,temperatureC=0,temperatureF=0,luminosity=0):
        self.temperatureC = temperatureC
        self.temperatureF = temperatureF
        self.luminosity = luminosity

    def setTemperatureInC(self, channel=0):
        # calculate temperature in degrees C
        self.temperatureC = channel/1024

    def setTemperatureInF(self, channel=0):
        # calculate temperature in degrees F
        self.temperatureF = ((channel/1024)*(9/5))+32

    def setLuminosity(self, channel=0):
        # calculate luminosity as a percentage
        self.luminosity = (channel-1850)/655

    def getTemperatureInC(self):
        # return temperature in C
        return self.temperatureC

    def getTemperatureInF(self):
        # return temperature in F
        return self.temperatureF

    def getLuminosity(self):
        # return luminosity as a percentage
        return self.luminosity
