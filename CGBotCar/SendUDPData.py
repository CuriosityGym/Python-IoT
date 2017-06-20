import socket 
 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
 
sock.sendto(bytes('HOLA', 'UTF-8'), ('192.168.1.9', 8888))
