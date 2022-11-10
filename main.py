from machine import freq

from config import WIFI_COUNTRY, WIFI_SSID, WIFI_PASS
from lib.http_server.http_server import start_server
import lib.wifi as wifi

wifi.config(WIFI_COUNTRY)

#region __main__
print(f'-- STARTED: CPU@{freq() / 1_000_000}MHz')

server_ip = wifi.connect_wifi(WIFI_SSID, WIFI_PASS)
start_server(server_ip)

print('-- EOF: main.py')
#endregion
