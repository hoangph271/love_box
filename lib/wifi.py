import network, rp2, socket, uasyncio
from config import *

rp2.country(WIFI_COUNTRY)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
# set power mode to get WiFi power-saving off (if needed)
# wlan.config(pm = 0xa11140) # type: ignore

def _filter_ips(ips):
    formatted_ips = ', '.join(ips)
    print(f'> IPs: {formatted_ips}')

    return next(ip for ip in ips if ip.startswith('192.168.'))

def scan_wifi():
    return wlan.scan()

async def host_wifi(ssid, password):
    ap = network.WLAN(network.AP_IF)

    ap.config(ssid=ssid, key=password)
    ap.active(True)

    while not ap.isconnected() and ap.status() == network.STAT_GOT_IP:
        print('> Creating AP...!')
        await uasyncio.sleep(1.25)

    print(f'> Created AP: {ssid}...!')
    return _filter_ips(ap.ifconfig())

async def join_wifi(ssid, password):
    wlan.connect(ssid, password)

    while not wlan.isconnected() and wlan.status() >= 0:
        print(f'> Joining AP [{ssid}]...!')
        await uasyncio.sleep(1.25)

    print(f'> Joined AP: {ssid}...!')
    return _filter_ips(wlan.ifconfig())

def open_socket(ip):
    connection = socket.socket() # type: ignore
    connection.bind((ip, 80))
    connection.listen(1)

    return connection
