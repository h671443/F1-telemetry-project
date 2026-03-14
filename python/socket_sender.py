import socket 

UDP_IP="127.0.0.1"
UDP_PORT= 5005

MESSAGE = b'\xe9\x07\x19\x01\x12\x01\x0cJ\xa0\x06!\xb2\x04Z\x9eQ'



 

print("sending packet")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

