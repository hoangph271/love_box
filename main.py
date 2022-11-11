from machine import freq
import machine

from config import *
from lib.http_server.http_server import start_server
import lib.wifi as wifi

wifi.config(WIFI_COUNTRY)

#region __main__
print(f'-- STARTED: CPU@{freq() / 1_000_000}MHz...!')

from lib.kv_db import init_db, get_json
init_db(KV_DB_DIR)
get_json('aps')

# ap_ip = wifi.host_wifi(AP_SSID, AP_PASS)

# server_ip = wifi.join_wifi(WIFI_SSID, WIFI_PASS)
# start_server(server_ip)

print('-- TERMINATED...!')
#endregion
