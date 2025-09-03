import socket


site = 'admin.html'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 60421))

    s.sendall(site.encode('utf-8'))
    data = s.recv(65535)
    print(f'Received {data.decode('utf-8')}')
