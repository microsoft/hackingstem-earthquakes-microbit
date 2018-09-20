
# ------------__ Hacking STEM – tuned_mass_damper.py – micro:bit __-----------
# For use with the Using Computational Thinking to Understand Earthquakes
# Lesson plan available from Microsoft Education Workshop at 
# http://aka.ms/hackingSTEM
#
#  Overview:
#  Uses of the micro:bit accelerometer to measure g force along the Y axis
#
#  This project uses a BBC micro:bit microcontroller, information at:
#  https://microbit.org/
#
#  Comments, contributions, suggestions, bug reports, and feature
#  requests are welcome! For source code and bug reports see:
#  http://github.com/[TODO github path to Hacking STEM]
#
#  Copyright 2018, Jeremy Franklin-Ross 
#  Microsoft EDU Workshop - HackingSTEM
#  MIT License terms detailed in LICENSE.md
# ===---------------------------------------------------------------===

from microbit import *

# loop interval
SLEEP_INTERVAL_MILLIS = 1

# End of line string
EOL="\n"

# The microbit analog scale factor for 8G
SCALE_FACTOR_8G = 0.00390625

# Constants for configuring accelerometer 
ACCELEROMETER = 0x1d
#ACC_2G = [0x0e, 0x00]  # not used, but useful reference
#ACC_4G = [0x0e, 0x01]  # not used, but useful reference 
ACC_8G = [0x0e, 0x02]   
CTRL_REG1_STANDBY = [0x2a, 0x00]
CTRL_REG_1_ACTIVE = [0x2a, 0x01]
XYZ_DATA_CFG = [0x0e]   # not used but useful reference

def command(c):
    """ send command to accelerometer """
    i2c.write(ACCELEROMETER, bytearray(c))

def i2c_read_acc(register):
    """ read accelerometer register """
    i2c.write(ACCELEROMETER, bytearray(register), repeat=True)
    read_byte = i2c.read(ACCELEROMETER, 1)
    # debug:
    # print('read: {}'.format(read_byte))
    return read_byte

# Set up & config
uart.init(baudrate=9600) # set serial data rate

# Configure accelerometer to 4G
command(CTRL_REG1_STANDBY)
command(ACC_8G)
command(CTRL_REG_1_ACTIVE)

uart.write(EOL+"0,"+EOL) # start with a clear line


""" Main program loop """
while (True):
    # Multiply Y reading by SCALE_FACTOR for 8G
    uart.write('{},'.format((accelerometer.get_y())*SCALE_FACTOR_8G)+EOL)
    sleep(SLEEP_INTERVAL_MILLIS)
