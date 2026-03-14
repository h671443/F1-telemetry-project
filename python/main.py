from listen import create_socket
import struct

sock = create_socket()

while True:
    data, addr = sock.recvfrom(2048) # F1 packets vary in size
   # print(list(data))
    
    year= struct.unpack_from("<HBB", data, 0)
    print(list(data))
    print (year)

