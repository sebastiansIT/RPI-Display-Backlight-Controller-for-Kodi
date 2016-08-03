#    Copyright 2016 Sebastian Spautz
#
#    This file is part of "RPI Display Backlight Control for Kodi".
#   
#    "RPI Display Backlight Control for Kodi" is free software: you can
#    redistribute it and/or modify it under the terms of the GNU General 
#    Public License as published by the Free Software Foundation, either 
#    version 3 of the License, or any later version.
#
#    "RPI Display Backlight Control for Kodi" is distributed in the hope 
#    that it will be useful, but WITHOUT ANY WARRANTY; without even the 
#    implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
#    See the GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.

import os
import xbmcaddon
 
addon             = xbmcaddon.Addon()
initialBrightness = addon.getSetting('rpi_backlight_brightness')
shellCommand      = 'echo ' + initialBrightness + ' > /sys/class/backlight/rpi_backlight/brightness'

os.system(shellCommand)
