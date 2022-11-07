from machine import Pin
import utime

import lib.config as config
import lib.network as network

led = Pin('LED', Pin.OUT)

led.on()

utime.sleep(1.25)

led.off()

network.connect_wifi()

print('exit(0)')
