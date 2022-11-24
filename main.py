import sys, machine, uasyncio

from config import *
from lib.http_server.http_server import start_server
from lib.led import led_on, led_off
import lib.wifi as wifi

async def main():
    print(f'-- STARTED: CPU@{machine.freq() / 1_000_000}MHz...!')
    led_on()

    await uasyncio.sleep(1)

    await wifi.host_wifi(AP_SSID, AP_PASS)
    server_ip = await wifi.join_wifi(WIFI_SSID, WIFI_PASS)

    start_server(server_ip)

    print('-- TERMINATING...!')
    led_off()
    sys.exit(0)

uasyncio.run(main())
