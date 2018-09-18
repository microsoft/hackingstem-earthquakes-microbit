
# ------------__ Hacking STEM – seismograph.py – micro:bit __-----------
# For use with the
# Lesson plan available from Microsoft Education Workshop at
# http://aka.ms/hackingSTEM
#
#  Overview:
#
#  This project uses a BBC micro:bit microcontroller, information at:
#  https://microbit.org/
#
#  Comments, contributions, suggestions, bug reports, and feature
#  requests are welcome! For source code and bug reports see:
#  http://github.com/[TODO github path to Hacking STEM]
#
#  Copyright 2018, Adi Azulay
#  Microsoft EDU Workshop - HackingSTEM
#  MIT License terms detailed in LICENSE.md
# ===---------------------------------------------------------------===

from microbit import *

dataSpeed = 75

# Setup & Config
display.off()  # Turns off LEDs to free up additional input pins
uart.init(baudrate=9600)  # Sets serial baud rate


def readSensors():
    sensorReading = pin0.read_analog()
    if sensorReading <= 3:
        sensorReading = 0
    sensorReading = sensorReading * 5  # TODO check scale factor against arduino version/workbook
    print(sensorReading)
    sleep(dataSpeed)
    sensorReading = -sensorReading
    print(sensorReading)
    sleep(dataSpeed)


while True:
    readSensors()
