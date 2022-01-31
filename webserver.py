import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Prepare a sever socket
PORT = 56027
s.bind(('', PORT))
s.listen()

while True:
    print('Ready to receive')
    connectionSocket, addr = s.accept()

    try:
        message = connectionSocket.recv(2048).decode()
        print("Message is ", message)
        headers = message.split('\n')
        fileName = headers[0].split()[1]
        fileName = fileName[1:]

        f = open(fileName)
        data = f.read()
        f.close()

        response = 'HTTP/1.1 200 OK\r\n' + data
        connectionSocket.send(response.encode())

        connectionSocket.close()
    except IOError:
        connectionSocket.send("HTTP/1.1 404 NOT FOUND\r\nFile not found".encode())
        connectionSocket.close()

s.close()
sys.exit()