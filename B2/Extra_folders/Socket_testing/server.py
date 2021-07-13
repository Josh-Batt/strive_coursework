import socket

# socket.AF_INET and SOCK_STREAM specifies this is a internet based connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.bind as this is the server.
# (()) because it needs to be a tuple
# ((IP address, port)) in this case IP is the host PC, the port can be any 4 digit number.
s.bind((socket.gethostname(), 2345))

# ??? How many times the server will interact with the client ???
s.listen(5)

# Check what the clients doing continuiously
while True:

    # clientsocket is the client side connection (socket)
    # address is the clients IP address
    # s.accept means we accept both the clients socket and their IP address
    clientsocket, address = s.accept()
    print(f'Connection from {address} has been established!')

    # Send something to the client side
    # ??? Has to be send in bytes ???
    # ??? bytes needs you to specify utf-8 as a argument ???
    clientsocket.send(bytes('Welcome to the server!', 'utf-8'))