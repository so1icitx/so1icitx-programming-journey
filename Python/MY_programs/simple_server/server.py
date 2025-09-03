import socket


HOST = '127.0.0.1'
PORT = 60421

sites = {'main.html':'the main', 'index.html':'the index', 'admin.html':'s3rtC'}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(((HOST, PORT)))
    s.listen()
    conn, addr = s.accept()


    with conn:
        ip = addr[0]
        port = addr[1]
        port = str(port)
        print(f'Connected to {ip}:{port}')
        while True:
            data = conn.recv(65535)
            data = data.decode('utf-8')
            if not data:
                break
            conn.sendall(sites[data].encode('utf-8'))




