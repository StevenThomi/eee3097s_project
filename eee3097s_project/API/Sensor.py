# Sensor class
class Sensor:
    def __init__(self,val_t=0,val_l=0,temperatureC=0,temperatureF=0,luminosity=0):
        self.val_t = val_t
        self.val_l = val_l
        self.temperatureC = temperatureC
        self.temperatureF = temperatureF
        self.luminosity = luminosity

    def setTemperatureInC(self, val_t):
        # calculate temperature in degrees C
        self.val_t = val_t
        self.temperatureC = self.val_t/1024

    def setTemperatureInF(self, val_t):
        # calculate temperature in degrees F
        self.val_t = val_t
        self.temperatureF = ((self.val_t/1024)*(9/5))+32

    def setLuminosity(self, val_l):
        # calculate luminosity as a percentage
        self.val_l = val_l
        self.luminosity = (self.val_l-1850)/655

    def getTemperatureInC(self):
        # return temperature in C
        return self.temperatureC

    def getTemperatureInF(self):
        # return temperature in F
        return self.temperatureF

    def getLuminosity(self):
        # return luminosity as a percentage
        return self.luminosity
