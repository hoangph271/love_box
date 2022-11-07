import network, rp2, utime

def connect_wifi(country, ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    rp2.country(country)

    # set power mode to get WiFi power-saving off (if needed)
    wlan.config(pm = 0xa11140)
    wlan.connect(ssid, password)

    while not wlan.isconnected() and wlan.status() >= 0:
        print("-- Waiting to connect:")
        utime.sleep(1.25)

    print(f'-- Connected to {ssid}, IPs:')
    print(wlan.ifconfig())
