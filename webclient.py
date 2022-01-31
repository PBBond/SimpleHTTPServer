import socket
import sys

HOST = sys.argv[1]
PORT = sys.argv[2]
fileName = sys.argv[3]
hostPort = f"{HOST}:{PORT}"
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, int(PORT)))

    message = f"GET /{fileName} HTTP/1.1"
    s.send(message.encode())

except IOError:
    print("Error")
    sys.exit(1)

response = s.recv(2048)
print(response.decode())
s.close()
