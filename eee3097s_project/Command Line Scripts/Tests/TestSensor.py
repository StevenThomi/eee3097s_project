# import math libraries (pi, sin, cos, atan2, sqrt) and dh22 sensor
import math
from dh22Sensor import dh22Sensor

# calculate distance in meters between two latitudinally and longitudinally
# defined spatial components
# implementation of the Haversine formula
# change the input formatted text into feedable input for
# distance calculation
def getDistanceFromLatLonInM(location1, location2):
    lat1 = int(location1[0:2]) + int(location1[4:6])/60 + float(location1[8:12])/3600
    lon1 = int(location1[16:18]) + int(location1[20:22])/60 + float(location1[24:28])/3600
    lat2 = int(location2[0:2]) + int(location2[4:6])/60 + float(location2[8:12])/3600
    lon2 = int(location2[16:18]) + int(location2[20:22])/60 + float(location2[24:28])/3600

    R = 6371000 # Earth's radius in m
    dLat = deg2rad(lat2-lat1)
    dLon = deg2rad(lon2-lon1)
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * math.sin(dLon/2) * math.sin(dLon/2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d

# convert degrees to radians
def deg2rad(deg):
    return deg * (math.pi/180)

def main():
    sensor1 = dh22Sensor()
    sensor2 = dh22Sensor()
    sensor3 = dh22Sensor()


    print("The following sensors have been registered: ")
    print("Sensor 1: ", end = "")
    sensor1.printSensor()

    print("\nSensor 2: ", end = "")
    sensor2.printSensor()

    print("\nSensor 3: ", end = "")
    sensor3.printSensor()

    print("\nStraight out the box. A configuration should get them up and running.")

    print("\nLet's initialize the sensors with some unique sensor IDs")

    newSensorID1 = input("Sensor 1 sensor ID: ")
    newSensorID2 = input("Sensor 2 sensor ID: ")
    newSensorID3 = input("Sensor 3 sensor ID: ")

    if(newSensorID1 == newSensorID2):
        print("Sensor ID is a unique field - sensor 1 and sensor 2 violation")
    elif(newSensorID2 == newSensorID3):
        print("Sensor ID is a unique field - sensor 2 and sensor 3 violation")
    elif(newSensorID1 == newSensorID3):
        print("Sensor ID is a unique field - sensor 1 and sensor 3 violation")
    else:
        sensor1.setSensorID(newSensorID1)
        sensor2.setSensorID(newSensorID2)
        sensor3.setSensorID(newSensorID3)

    print("\nAlmost done. Where would you like to situate them?")
    print("\nAbide by format: 00° 00\' 00.0\" S 00° 00\' 00.0\" E")

    newLocation1 = input("Input sensor 1's location (lattitude, longitude): ").strip()
    newLocation2 = input("Input sensor 2's location (lattitude, longitude): ").strip()
    newLocation3 = input("Input sensor 3's location (lattitude, longitude): ").strip()

    sensor1.setLocation(newLocation1)
    sensor2.setLocation(newLocation2)
    sensor3.setLocation(newLocation3)

    print("\nAfter 5 minutes, their states are checked once more: ")
    print("\nSensor 1: Temperature = ", sensor1.getTemperature())
    print("Sensor 1: Humidity = ", sensor1.getHumidity())
    print("Sensor 1: Alert = " + str(sensor1.getAlert()))

    print("\nSensor 2: Temperature = ", sensor2.getTemperature())
    print("Sensor 2: Humidity = ", sensor2.getHumidity())
    print("Sensor 2: Alert = " + str(sensor2.getAlert()))

    print("\nSensor 3: Temperature = ", sensor3.getTemperature())
    print("Sensor 3: Humidity = ", sensor3.getHumidity())
    print("Sensor 3: Alert = " + str(sensor3.getAlert()))

    distance12 = getDistanceFromLatLonInM(newLocation1, newLocation2)
    distance23 = getDistanceFromLatLonInM(newLocation2, newLocation3)
    distance13 = getDistanceFromLatLonInM(newLocation1, newLocation3)

    print("\n\nThe distance between sensor 1 and sensor 2 is: ", distance12, "m")
    print("\nThe distance between sensor 2 and sensor 3 is: ", distance23, "m")
    print("\nThe distance between sensor 1 and sensor 3 is: ", distance13, "m")

# ideally, the distance between sensors should range between 5 and 15
    if(distance12 > 50 or distance12 < 10):
        print("\nsensor 1 and sensor 2 are innefectively spaced")
    else:
        print("\nThe spacing between sensor 1 and sensor 2 is exquisite! Good job.")

    if(distance23 > 50 or distance23 < 10):
        print("\nsensor 2 and sensor 3 are innefectively spaced")
    else:
        print("\nThe spacing between sensor 2 and sensor 3 is exquisite! Good job.")

    if(distance13 > 50 or distance13 < 10):
        print("\nsensor 1 and sensor 3 are innefectively spaced")
    else:
        print("\nThe spacing between sensor 1 and sensor 3 is exquisite! Good job.")

main() # Call the main function
