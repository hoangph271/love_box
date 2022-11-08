import wifi, led
from http_helper import send_ok, send_text, send_404

def start_server(server_ip):
    connection = wifi.open_socket(server_ip)

    print(f'-- Started server at: http://{server_ip}:80')
    led.led_on()

    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        url = request.split()[1]

        if url.startswith('/led_on'):
            led.led_on()
            send_ok(client)
        elif url.startswith('/led_off'):
            led.led_off()
            send_ok(client)
        elif url == '/':
            readme_fd = open('README.md', 'r')
            send_text(client, readme_fd.read(), 'text/markdown')
            readme_fd.close()
        elif url.startswith('/exit'):
            send_ok(client)
            break
        else:
            print(f'- Unhandled URL: {url}')
            send_404(client)
