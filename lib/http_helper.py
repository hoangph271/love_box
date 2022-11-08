def send_ok(client):
    client.send(f'HTTP/1.1 200 OK\nContent-Type: text/plain\n\n200 | Ok')
    client.close()

def send_404(client):
    client.send(f'HTTP/1.1 200 OK\nContent-Type: text/plain\n\n404 | Not Found')
    client.close()

def send_text(client, content, content_type = 'text/plain'):
    client.send(f'HTTP/1.1 200 OK\nContent-Type: {content_type}\n\n{content}')
    client.close()
