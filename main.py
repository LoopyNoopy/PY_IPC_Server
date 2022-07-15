from multiprocessing.connection import Listener

address = ('localhost', 6000)     # family is deduced to be 'AF_INET'
listener = Listener(address, authkey=b'blah')
print("running")

while True:
    conn = listener.accept()
    print('connection accepted from', listener.last_accepted)
    msg = conn.recv()
    print(msg)
    # do something with msg
    if msg == 'close':
        conn.close()
        break
listener.close()