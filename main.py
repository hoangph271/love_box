from machine import freq
import machine

from config import *
from lib.http_server.http_server import start_server
import lib.wifi as wifi

wifi.config(WIFI_COUNTRY)

#region __main__
print(f'-- STARTED: CPU@{freq() / 1_000_000}MHz...!')

ap_ip = wifi.host_wifi(AP_SSID, AP_PASS)

server_ip = wifi.join_wifi(WIFI_SSID, WIFI_PASS)
start_server(server_ip)

print('-- TERMINATED...!')
#endregion
