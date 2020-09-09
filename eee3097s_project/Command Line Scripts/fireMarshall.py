# import Enum class library, and User class
from enum import Enum, unique
from User import User

@unique
class FireStation(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4
    CENTER = 5

# define the fire marshall user type
class FireMarshall(User):
    def __init__(self, station = 1):
        super().__init__()
        self.__station = FireStation(station)

# select a station in the lookup table
    def setStation(self, station):
        if(5 < station > 1):
            self.__station = FireStation(station)
        else:
            print("Error... revert to default")
            self.__station = FireStation(1)

    def getStation(self):
        return self.__station

# display fire marshall attributes
    def printFireMarshall(self):
        print(self.__str__() + ", Station: " + str(self.__station))
