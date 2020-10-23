import socket

HOST = str(input("Host's IP:\n"))  # The server's hostname or IP address
PORT = 4444        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'hi')
    data = s.recv(1024)

print(data.decode())
