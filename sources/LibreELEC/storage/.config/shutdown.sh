case "$1" in
   halt)
      ;;
   poweroff)
      if [ -e /sys/class/backlight/rpi_backlight/bl_power ]
      then
         echo 1 > /sys/class/backlight/rpi_backlight/bl_power
      fi
      ;;
   reboot)
      ;;
   *)
      ;;
esac
