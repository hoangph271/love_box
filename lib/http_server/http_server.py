import wifi, led, motors
from http_server.http_response import send_ok, send_text, send_404, send_301
from fs_helper import read_text_file

def _handle_ui_command(ui_command, client):
    if ui_command.startswith('/led_on'):
        led.led_on()
    elif ui_command.startswith('/led_off'):
        led.led_off()
    elif ui_command.startswith('/motors/forward_left'):
        motors.forward_left()
    elif ui_command.startswith('/motors/forward_right'):
        motors.forward_right()
    elif ui_command.startswith('/motors/backward_left'):
        motors.backward_left()
    elif ui_command.startswith('/motors/backward_right'):
        motors.backward_right()
    elif ui_command.startswith('/motors/stop_left'):
        motors.stop_left()
    elif ui_command.startswith('/motors/stop_right'):
        motors.stop_right()
    elif ui_command.startswith('/motors/stop'):
        motors.stop_both()

    html = read_text_file('lib/index.html')
    send_text(client, html, 'text/html')

    print(f'Handled UI command: {ui_command}')

def start_server(server_ip):
    connection = wifi.open_socket(server_ip)

    print(f'> Started server at: http://{server_ip}:80')
    led.led_on()

    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        # TODO: parse request for METHOD, also
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
