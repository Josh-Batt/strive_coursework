import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.connect((socket.gethostname(), 1342))
s.connect(('37.162.13.150', 1342))
msg = s.recv(1024)
print(msg.decode('utf-8'))