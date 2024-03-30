import socket
import cv2
import pickle
import struct
import ssl
from threading import Thread

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '192.168.1.9'
port = 5005
socket_address = (host_ip, port)
print('HOST IP:', host_ip)
print("port:", port)
print('Socket created')

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server_cert.pem", keyfile="server_key.pem")
server_socket = context.wrap_socket(server_socket, server_side=True)

server_socket.bind(socket_address)
print('Socket bind complete')

server_socket.listen(5)
print('Socket now listening')

while True:
    client_socket, addr = server_socket.accept()
    print('Connection from:', addr)
    vid = cv2.VideoCapture(0)
    while vid.isOpened():
        img, frame = vid.read()
        a = pickle.dumps(frame)
        message = struct.pack("Q", len(a)) + a
        client_socket.sendall(message)
        cv2.imshow('Sending...', frame)
        key = cv2.waitKey(10)
        if key == 13:
            break
    client_socket.close()

