from config import WIFI_COUNTRY, WIFI_SSID, WIFI_PASS

import lib.network as network

network.connect_wifi(WIFI_COUNTRY, WIFI_SSID, WIFI_PASS)
