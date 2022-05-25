import socket

s = socket.socket()
port = 12345
s.connect(('127.0.0.1', port))
s.send(("POST /test HTTP/1.1\nHost: 127.0.0.1\n\nmsg=Hello World").encode())
r = s.recv(1024).decode()
print(r)
s.close()
