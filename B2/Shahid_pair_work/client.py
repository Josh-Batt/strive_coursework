import socket
import pickle
import time

HEADERSIZE = 10
PORT = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), PORT))

while True:
    d = {'lat': 84, 'lon': 64, 'time': time.time()}
    msg = pickle.dumps(d)
    time.sleep(3)
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', 'utf-8') + msg
    s.send(msg)