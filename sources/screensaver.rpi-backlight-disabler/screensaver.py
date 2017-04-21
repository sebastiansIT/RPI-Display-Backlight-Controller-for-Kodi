#    Copyright 2016 Sebastian Spautz <sebastian@human-injection.de>
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

import xbmcaddon
import xbmcgui
import xbmc
import os

addon = xbmcaddon.Addon()
addonName = addon.getAddonInfo('name')
addonPath = addon.getAddonInfo('path')

class Screensaver(xbmcgui.WindowXMLDialog):

    class ExitMonitor(xbmc.Monitor):

        def __init__(self, exit_callback):
            self.exit_callback = exit_callback

        def onScreensaverDeactivated(self):
            self.exit_callback()

    def prepareShellCommand(self, command):
        if os.geteuid() != 0:
            self.log('Don\'t root, try sudo to toggle backlight.')
            return 'sudo bash -c \'' + command + '\''
        else:
            return command;

    def onInit(self):
        self.log('Start Screensaver')
        self.exit_monitor = self.ExitMonitor(self.exit)
        shellCommand = self.prepareShellCommand('echo 1 > /sys/class/backlight/rpi_backlight/bl_power')
        os.system(shellCommand)

    def exit(self):
        self.exit_monitor = None
        shellCommand = self.prepareShellCommand('echo 0 > /sys/class/backlight/rpi_backlight/bl_power')
        os.system(shellCommand)
        self.close()
        self.log('Stopped Screensaver')

    def log(self, msg):
        xbmc.log(u'%(name)s: %(message)s' % {'name': addonName, 'message': msg})

if __name__ == '__main__':
    screensaver = Screensaver(
        'screensaver-%s-Main.xml' % addonName.replace(' ', ''),
        addonPath,
        'default',
    )
    screensaver.doModal()
    del screensaver
    sys.modules.clear()