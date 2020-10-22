from Sensor import Sensor
from Setup import Setup
from time import sleep

def main():
    while True:
        # Create Setup object
        bus = Setup()

        # Create Sensor object
        sense = Sensor()

        # Setup the SPI bus
        bus.busSetup()

        # Retrieve the SPI bus
        value1, value2 = bus.getBus()

        # Setup the sensors
        sense.setTemperatureInC(value1)

        sense.setTemperatureInF(value1)

        sense.setLuminosity(value2)

        # Fetch temperature in degrees C
        temperatureC = sense.getTemperatureInC()

        # Fetch temperature in degrees F
        temperatureF = sense.getTemperatureInF()

        # Fetch luminosity as a percentage
        luminosity = sense.getLuminosity()

        # print output
        print("Temperature in degrees Celsius: {:5.2f} deg".format(temperatureC))

        print("Temperature in degrees Fahrenheit: {:5.2f} deg".format(temperatureF))

        print("Luminosity as a percentage: {:6.2f} %".format(luminosity))

        print("\n")

        # time delay between readings
        sleep(1)

main() # call the main function