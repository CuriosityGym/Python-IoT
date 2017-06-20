import socket

UDP_IP = "192.168.4.2"
UDP_PORT = 1111
#print("A")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    #print("B")
    data, addr = sock.recvfrom(7) # buffer size is 1024 bytes
    print ("received message:", data)
