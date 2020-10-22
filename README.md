# Engineering Design Project

## Electrical and Computer Engineering Practical Design and Implementation

## Aim:
Using a small single-board computer, develop an IoT application to generate a temperature and humidity mapping of a wide geographical location.

## Use Case:
The temperature and humidity mapping can be used to identify forest fires through:
- identifying temperature spikes
- identifying humidity dips

## Problems encountered in development:
As a result of lacking a temperature-controlled solder iron, oscilloscope, or a dedicated multimeter, my troubleshooting process has been greatly hindered. 

The sensor has proven to be faulty; the power ON LED fails to work for the default logic level (3V3). 

The I2C protocol as well has been enhanced, to enable a sleep-mode operation of the sensor - to reduce operational heating. The libraries required to jump start the sensor's I2C configuration are available on Wire.h (an Arduino library), but not availabe on WiringPi (the Raspberry Pi equivalent libraries). The soldered surface-mount jumpers facilitate a change of interface to the One-Wire configuration; which I would have preferred due to its improved standardisation.

## Alternate Theory:
As enhanced in the  tools list below, the analog input sensors - the Light Dependent Resistor, and the MCP9700 Temperature Sensor - have taked a forefront in my development effort, and my attempt to satisfactorily meet the use case.

The temperature and light intensity mapping can be used to identify forest fires through:
- identifying temperature spikes
- identifying persevering light intensity changes

To further explain the last point; in sunny parts of the forest the sunlight light intensity overbears the flame light intensity, causing the observable change to be in the smoke particle density, while in darker parts of the forest the absence of sunlight light intensity causes the flame light intensity to be a more observable change.

## Tools:
>“A man is only as good as his tools.”  
*― Emmert Wolf*

The following tools are at my disposal:
- 1x CM2322 Temperature and Humidity Sensor
- 1x Raspberry Pi Zero W
- 1x 40 way Male-Male ribbon strip
- 1x 40 way Male-Female ribbon strip
- 1x MCP3008 Analog to Digital Converter
- 1x EEPROM Storage
- 2x Through-hole Pushbutton
- 1x Breadboard
- 4x Red LED
- 10x 1k Through-hole 0.25W Resistor
- 10x 10k Through-hole 0.25W Resistor
- 1x **Light Dependent Resistor**
- 1x **MCP9700 Temperature Sensor**
- 2x 2222A NPN Transistor
- 1x Piezo Buzzer
- 1x MicroSD Card Reader
