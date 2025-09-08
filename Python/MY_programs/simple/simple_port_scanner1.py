import socket
ip = '8.8.8.8'

def main():
    for i in range(1, 65536):
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((ip, i))
            print(f'{ip}:{i}')
        except Exception:
            pass
        finally:
            sock.close()



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nExiting')

