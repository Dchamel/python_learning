# socket
# provides access to the BSD-interface, working with network, etc...

# TCP/IP Server
import socket

# crete TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect soket to a port
server_address = ('localhost', 9999)
print('connecting to {0} port {1}'.format(*server_address))
sock.bind(server_address)

# Listen input connections
sock.listen()

while True:
    print('waiting for connection...')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        while True:
            data = connection.recv(16)
            print(f'received: {data.decode()} ')
            if data:
                print(f'data processing...')
                data = data.upper()
                print('sending data to receiver...')
                connection.sendall(data)
            else:
                print('no data', )
    except ConnectionRefusedError:
        print('connection refused!')
    finally:
        connection.close()

# TCP/IP CLient
