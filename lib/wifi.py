import network, rp2, utime, socket

def config(country):
    rp2.country(country)

def host_wifi(ssid, password):
    ap = network.WLAN(network.AP_IF)

    ap.config(ssid=ssid, key=password)
    ap.active(True)

    while not ap.isconnected() and ap.status() == network.STAT_GOT_IP:
        print('-- Creating AP...!')
        utime.sleep(1.25)

    return next(ip for ip in ap.ifconfig() if ip.startswith('192.168.'))

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # set power mode to get WiFi power-saving off (if needed)
    wlan.config(pm = 0xa11140) # type: ignore
    wlan.connect(ssid, password)

    while not wlan.isconnected() and wlan.status() >= 0:
        print('-- Connecting...!')
        utime.sleep(1.25)

    return next(ip for ip in wlan.ifconfig() if ip.startswith('192.168.'))

def open_socket(ip):
    connection = socket.socket() # type: ignore
    connection.bind((ip, 80))
    connection.listen(1)

    return connection
