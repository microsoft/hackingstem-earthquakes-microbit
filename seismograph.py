
# ------------__ Hacking STEM – seismograph.py – micro:bit __-----------
# For use with the Using Computational Thinking to Understand Earthquakes
# Lesson plan available from Microsoft Education Workshop at
# https://education.microsoft.com/hackingStem/lesson/088ef496
# http://aka.ms/hackingSTEM
#
#  Overview:
#  This code reads an analog pin scales up the reading, and write to serial
#  the reading in the opposite of the reading.
#
#  This project uses a BBC micro:bit microcontroller, information at:
#  https://microbit.org/
#
#  Comments, contributions, suggestions, bug reports, and feature
#  requests are welcome! For source code and bug reports see:
#  https://github.com/microsoft/hackingstem-earthquakes-microbit
#
#  Copyright 2018, Adi Azulay
#  Microsoft EDU Workshop - HackingSTEM
#  MIT License terms detailed in LICENSE.txt
# ===---------------------------------------------------------------===

from microbit import *

# Frequency of code looping
dataSpeed = 75

# End of Line Character
EOL='\n'

# Setup & Config
display.off()  # Turns off LEDs to free up additional input pins
uart.init(baudrate=9600)  # Sets serial baud rate


def readSensors():
    sensorReading = pin0.read_analog()
    # Filter out low readings to 0
    if sensorReading <= 3:
        sensorReading = 0
    sensorReading = sensorReading * 3
    uart.write('{},'.format(sensorReading)+EOL)
    sleep(dataSpeed)
    sensorReading = -sensorReading
    uart.write('{},'.format(sensorReading)+EOL)
    sleep(dataSpeed)


while True:
    readSensors()
