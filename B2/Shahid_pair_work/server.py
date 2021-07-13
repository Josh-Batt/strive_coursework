import socket
import pickle
import csv

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 3000))
s.listen(1)
while True:
    client_socket, address = s.accept()
    print(f'Connection from {address} has been established')
    full_msg = b''
    new_msg = True
    while True:
        msg = client_socket.recv(16)
        if new_msg:
            print(f'new message legnth:{msg[:HEADERSIZE]}')
            msg_len = int(msg[:HEADERSIZE])
            new_msg = False
        full_msg += msg
        if len(full_msg) - HEADERSIZE == msg_len:
            print('Full msg recvd')
            print(full_msg[HEADERSIZE:])
            print(pickle.loads(full_msg[HEADERSIZE:]))
            fields = ['lat', 'lon', 'time']
            with open(r'test2.csv', 'a', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writerow(pickle.loads(full_msg[HEADERSIZE:]))
            new_msg = True
            full_msg = b''