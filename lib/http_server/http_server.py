import wifi, led
from http_server.http_response import send_ok, send_text, send_404, send_301
from fs_helper import read_text_file

def _handle_ui_command(ui_command, client):
    if ui_command.startswith('/led_on'):
        led.led_on()
    elif ui_command.startswith('/led_off'):
        led.led_off()

    html = read_text_file('lib/index.html')
    send_text(client, html, 'text/html')

def start_server(server_ip):
    connection = wifi.open_socket(server_ip)

    print(f'> Started server at: http://{server_ip}:80')
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
        elif url.startswith('/exit'):
            send_ok(client)
            break
        elif url.startswith('/ui'):
            ui_command = url[len('/ui'):]
            _handle_ui_command(ui_command, client)
        elif url == '/README.md':
            send_text(client, read_text_file('README.md'), 'text/markdown')
        elif url == '/favicon.ico':
            send_301(client, 'https://sneu.date/static/svg/sneu.svg')
        elif url == '/':
            send_301(client, '/ui')
        else:
            print(f'- Unhandled URL: {url}')
            send_404(client)
