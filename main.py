from machine import freq

from config import WIFI_COUNTRY, AP_PASS, AP_SSID
from lib.http_server.http_server import start_server
import lib.wifi as wifi

wifi.config(WIFI_COUNTRY)

#region __main__
print(f'-- STARTED: CPU@{freq() / 1_000_000}MHz')

server_ip = wifi.host_wifi(AP_SSID, AP_PASS)
start_server(server_ip)

print('-- EOF: main.py')
#endregion
