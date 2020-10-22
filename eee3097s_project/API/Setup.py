# ADC (MCP3008) support libraries
# Busio is the SMBus equivalent bus
# for our configuration
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

class Setup:
    def __init__(self):
        self.analogIn1 = 0
        self.analogIn2 = 0

    def busSetup(self): 
        # Setting up the ADC SPI interface
        # create the spi bus
        spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
 
        # create the cs (chip select)
        cs1 = digitalio.DigitalInOut(board.D5)
        cs2 = digitalio.DigitalInOut(board.D2)
 
        # create the mcp objects
        mcp1 = MCP.MCP3008(spi, cs1)
        mcp2 = MCP.MCP3008(spi, cs2)

        # retrieve analog input channel on pin 0, and pin 1
        analogIn1 = AnalogIn(mcp1, MCP.P0)
        analogIn2 = AnalogIn(mcp2, MCP.P1)

        # return analog input
        self.analogIn1 = analogIn1.value
        self.analogIn2 = analogIn2.value

    def getBus(self):
       # retrieve SPI bus
       return self.analogIn1, self.analogIn2
