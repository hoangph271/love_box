from config import WIFI_COUNTRY, WIFI_SSID, WIFI_PASS
import lib.network as network
import lib.led as led

server_ip = network.connect_wifi(WIFI_COUNTRY, WIFI_SSID, WIFI_PASS)
connection = network.open_socket(server_ip)

def send_ok(client):
    client.send(f'HTTP/1.1 200 OK\nContent-Type: text/plain\n\n200 | Ok')
    client.close()

def send_404(client):
    client.send(f'HTTP/1.1 200 OK\nContent-Type: text/plain\n\n404 | Not Found')
    client.close()

def send_text(client, content):
    client.send(f'HTTP/1.1 200 OK\nContent-Type: text/plain\n\n{content}')
    client.close()

def serve(connection):
    print(f'-- Started server at: http://{server_ip}:80')
    led.led_on()

    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        url = request.split()[1]

        if url.startswith('/led_on'):
            led.led_on()
        elif url.startswith('/led_off'):
            led.led_off()
        elif url.startswith('/exit'):
            send_ok(client)
            break
        else:
            print(f'- Unhandled URL: {url}')
            send_404(client)
            continue

        send_ok(client)

serve(connection)

print('-- EOF: main.py')
