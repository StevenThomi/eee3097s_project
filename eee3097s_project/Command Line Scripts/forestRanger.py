# import Enum class library, and User class
from enum import Enum, unique
from User import User

@unique
class Forest(Enum):
    AMAZON = 1
    CONGO = 2
    BURMESE = 3
    BORNEO = 4
    VALDIVIAN = 5

# define the forest ranger user type
class ForestRanger(User):
    def __init__(self, forest = 1):
        super().__init__()
        self.__forest = Forest(forest)

# select a forest in the lookup table
    def setForest(self, forest):
        if(forest >= 1 and forest <= 5):
            self.__forest = Forest(int(forest))
        else:
            print("Error... revert to default")
            self.__forest = Forest(1)

    def getForest(self):
        return self.__forest

# display forest ranger attributes
    def printRanger(self):
        print(self.__str__() + ", Forest: " + str(self.__forest))
