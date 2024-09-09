# socket
# provides access to the BSD-interface, working with network, etc...

# ---

# TCP/IP Server

# import socket
#
# # crete TCP/IP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # connect soket to a port
# server_address = ('localhost', 9999)
# print('connecting to {0} port {1}'.format(*server_address))
# sock.bind(server_address)
#
# # Listen input connections
# sock.listen()
#
# while True:
#     print('waiting for connection...')
#     connection, client_address = sock.accept()
#     try:
#         print('connection from', client_address)
#         while True:
#             data = connection.recv(16)
#             print(f'received: {data.decode()} ')
#             if data:
#                 print(f'data processing...')
#                 data = data.upper()
#                 print('sending data to receiver...')
#                 connection.sendall(data)
#             else:
#                 print('no data', )
#     except ConnectionRefusedError:
#         print('connection refused!')
#     finally:
#         connection.close()

# ---

# TCP/IP Client

# import socket, sys
#
# # create IP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # connect socket to port
# server_address = ('localhost', 9999)
# print('connecting to {} port {}'.format(*server_address))
# sock.connect(server_address)
#
# try:
#     # send data
#     mess = 'Hello World!'
#     print('sending "{}"'.format(mess))
#     message = mess.encode('utf-8')
#     sock.sendall(message)
#
#     # check answer
#     amount_received = 0
#     amount_expected = len(message)
#     while amount_received < amount_expected:
#         data = sock.recv(16)
#         amount_received += len(data)
#         mess = data.decode('utf-8')
#         print('received {} bytes'.format(mess))
# finally:
#     print('closing socket')
#     sock.close()

# ---------

# mimetypes
# converts filename or Url to MIME-type

# import mimetypes
#
# mime_type, encoding = mimetypes.guess_type('http://docs.python.org/3/library/mimetypes.html')
# # extension = mime_type.split('/')[-1]
# # extension = mimetypes.guess_extension(mime_type)
# print(mime_type)

# --------

# smtplib
# for sending emails via smtp

# import smtplib

# ---------

# urllib
# all work with http/https

# import urllib.request as request
# import urllib.parse as parse

# ---------

# ssl
# this module provides instruments for work with ssl

# import ssl
#
# def create_ssl_context():
#     ctx = ssl.create_default_context()
#     ctx.check_hostname = False
#     ctx.verify_mode = ssl.CERT_NONE
#     return ctx
#
#
# # forming request to geocoder
# req = urllib_request(url_, {'Address': 'geocoding-service.sbrf.ru', 'outFields': 'Addr_type', 'f': 'pjson'})
# response = request.urlopen(req, context=create_ssl_context())
# result = urllib_parser(response, 'candidates')

# ---

# check valid

import ssl, socket

# create ssl context
context = ssl.create_default_context()

# setup ssl-check policy
context.check_hostname = True
context.verify_mode = ssl.CERT_REQUIRED

# check valid
try:
    with socket.create_connection(('example.com', 443)) as sock:
        with context.wrap_socket(sock, server_hostname='example.com') as ssock:
            cert = ssock.getpeercert()
            subject = dict(x[0] for x in cert['subject'])
            common_name = subject['commonName']
            print(f'Sert valid for: {common_name}')
except ssl.SSLError as e:
    print(f'Error checking SSL: {e}')
