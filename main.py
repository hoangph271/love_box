from machine import freq

from config import WIFI_COUNTRY, WIFI_SSID, WIFI_PASS
import lib.wifi as wifi
import lib.http_server as http_server

# import lib.led as led
# from lib.http_helper import send_ok, send_404, send_text

wifi.config(WIFI_COUNTRY)

#region __main__

print(f'-- Running at {freq() / 1_000_000} MHz')

server_ip = wifi.connect_wifi(WIFI_SSID, WIFI_PASS)
http_server.start_server(server_ip)

print('-- EOF: main.py')
#endregion
