#!/usr/bin/python

import os
import argparse

def disableBacklight():
    os.system('echo 1 > /sys/class/backlight/rpi_backlight/bl_power')
    
def enableBacklight():
    os.system('echo 0 > /sys/class/backlight/rpi_backlight/bl_power')
    
def setBrightness( brightness ):
    os.system('echo ' + str(brightness) + ' > /sys/class/backlight/rpi_backlight/brightness')
    
parser = argparse.ArgumentParser(description='Manipulate the Backlight of the Offical Raspberry Pi 7" Touch Display.')
parser.add_argument('-b', '--brightness', dest='brightness', nargs='?', default=255, type=int, choices=range(0, 256), help='Set the brightness of the display betwean 0 and 255')
parser.add_argument('-p', '--power', dest='power', nargs='?', default=1, type=int, choices=[0,1], help='Activate (1) or deactivate (0) the backlight')

args = parser.parse_args()
print args.power
print args.brightness
if args.power == 0:
    disableBacklight()
else:
    enableBacklight()
setBrightness(args.brightness)