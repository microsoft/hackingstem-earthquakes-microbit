
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
#  MIT License terms detailed in LICENSE.txt
# ===---------------------------------------------------------------===

from microbit import *

# The microbit analog scale factor for 8G
SCALE_FACTOR_8G = 0.00390625

def command(a, c):
    """ send command to accelerometer """
    i2c.write(a, bytearray(c))

def i2c_read(a, register):
    """ read accelerometer register """
    i2c.write(a, bytearray(register), repeat=True)
    read_byte = i2c.read(a, 1)
    return read_byte

# Detect accelerometer variant and configure accelerometer to 8G
MMA8653_ACCEL = 0x1d
LSM303_ACCEL = 0x19 
FXOS8700_ACCEL = 0x1E 

i2c_addresses = i2c.scan()

if (MMA8653_ACCEL in i2c_addresses and 
		i2c_read(MMA8653_ACCEL, [0x0D]) == bytes([0x5A])):
	command(MMA8653_ACCEL, [0x2a, 0x00]) # STAND BY
	command(MMA8653_ACCEL, [0x0e, 0x02]) # SET 8G
	command(MMA8653_ACCEL, [0x2a, 0x01]) # ACTIVE
elif (LSM303_ACCEL in i2c_addresses and
		i2c_read(LSM303_ACCEL, [0x0F]) == bytes([0x33])):
	command(LSM303_ACCEL, [0x23, 0x80 |  0x20 ]) #SET 8G
elif (FXOS8700_ACCEL in i2c_addresses and
		i2c_read(FXOS8700_ACCEL, [0x0D]) == bytes([0xC7])):
	command(FXOS8700_ACCEL, [0x0E, 0x2]) # UNTESTED! SET 8G
else:
	while True:
		display.scroll("Unsupported microbit model", delay=90, loop=True)

# loop interval
SLEEP_INTERVAL_MILLIS = 1

# End of line string
EOL="\n"

# Set up & config
uart.init(baudrate=9600) # set serial data rate
uart.write(EOL+"0,"+EOL) # start with a clear line

""" Main program loop """
while (True):
    # Multiply Y reading by SCALE_FACTOR for 8G
    uart.write('{},'.format((accelerometer.get_y())*SCALE_FACTOR_8G)+EOL)
    sleep(SLEEP_INTERVAL_MILLIS)
