from enum import Enum, unique
from random import randint

@unique
class FireStation(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4
    CENTER = 5

class FireMarshall(User):
    def __init__(self, station = 1):
        super().__init__()
        self.__marshallID = randint(0,1000)
        self.__station = FireStation(station)

    def setMarshallID(self):
        self.__rangerID = randint(0,1000)

    def setStation(self, station):
        if(5 < station > 1):
            self.__station = FireStation(forest)
        else:
            print("Error... revert to default")
            self.__station = FireStation(1)
            
    def getMarshallID(self):
        return self.__marshallID

    def getStation(self, name):
        return self.__station

    def printMarshall(self):
        print(", " + self.__str__() + "Marshall ID: " + self.__marshallID + \
                ", Station: " + self.__station)
