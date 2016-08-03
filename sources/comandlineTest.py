#!/usr/bin/python

import os
# import subprocess

# brightnessDevice = open('/sys/devices/platform/rpi_backlight/backlight/rpi_backlight/brightness', 'w')
# subprocess.call(["echo", "150"], stdout=brightnessDevice)

os.system('echo 50 > /sys/class/backlight/rpi_backlight/brightness')

