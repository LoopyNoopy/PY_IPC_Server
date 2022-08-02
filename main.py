from multiprocessing.connection import Client
from multiprocessing.connection import Listener
import random

def IPCSend(value):
    IPCAddress = ('localhost',7000)
    global connection
    connection = Client(IPCAddress,authkey=b'blah')
    connection.send(value)
    connection.send("close")
    connection.close()
    return()

address = ('localhost', 6000)     # family is deduced to be 'AF_INET'
listener = Listener(address, authkey=b'blah')
print("running")

def IPCRequest(msg):
    match msg:
        case "background":
            number_of_colors = 1
            color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                     for i in range(number_of_colors)]
            print("Colour Generated: " + str(color))
            IPCSend(color)
            return "background"
    return(msg)

while True:
    conn = listener.accept()
    print('connection accepted from', listener.last_accepted)
    msg = conn.recv()
    IPCRequest(msg)
    # do something with msg
    if msg == 'close':
        conn.close()
        break
listener.close()

