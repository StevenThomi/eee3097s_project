from enum import Enum, unique
from random import randint

@unique
class Forest(Enum):
    AMAZON = 1
    CONGO = 2
    BURMESE = 3
    BORNEO = 4
    VALDIVIAN = 5

class ForestRanger(User):
    def __init__(self, forest = 1):
        super().__init__()
        self.__rangerID = randint(0,1000)
        self.__forest = Forest(forest)

    def setRangerID(self):
        self.__rangerID = randint(0,1000)

    def setForest(self, forest):
        if(5 < forest > 1):
            self.__forest = Forest(forest)
        else:
            print("Error... revert to default")
            self.__forest = Forest(1)

    def getRangerID(self):
        return self.__rangerID

    def getForest(self, name):
        return self.__forest

    def printRanger(self):
        print(", " + self.__str__() + "Ranger ID: " + self.__rangerID + \
                ", Forest: " + self.__forest)
