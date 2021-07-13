import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.connect as the client wants to connect to the server socket
# *** socket.gethostbyname() MAY be the answer we need to connect with eachother!
s.connect((socket.gethostname(), 2345))

# Client side accepting msg from server side
# .recv = recive
# (1024) is the buffer we want. msg is a stream of data, 
# 1024 specifies how much of this data we want to recive at a time 
msg = s.recv(1024)

# Info from server sent as bytes
# .decode = Decoding the bytes
print(msg.decode('utf-8'))