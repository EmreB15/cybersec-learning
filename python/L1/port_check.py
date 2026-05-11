import socket


def check_port(host, port, timeout=1.0):
    try:
        socket_1 = socket.create_connection((host, port), timeout)
    except OSError:
        return False
    socket_1.close()
    return True

ip = "127.0.0.1"
ports = [8080, 9999]
for port in ports:
    if check_port(ip, port):
        print(ip + ":" + str(port) + " - OPEN")
    else:
        print(ip + ":" + str(port) + " - CLOSED")
