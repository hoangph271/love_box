from config import WIFI_COUNTRY, WIFI_SSID, WIFI_PASS
import lib.network as network
import lib.led as led

network.connect_wifi(WIFI_COUNTRY, WIFI_SSID, WIFI_PASS)

led.led_on()
