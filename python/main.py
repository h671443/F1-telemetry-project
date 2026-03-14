from listen import create_socket
import struct

sock = create_socket()


while True:
    data, addr = sock.recvfrom(2048) # F1 packets vary in size
   # print(list(data))
    
    header_values=struct.unpack_from("<HBBBBBQfLLBB", data, 0)

    header = {
    "packet_format": header_values[0],
    "game_year": header_values[1],
    "Version": header_values[2],
    "minor_version": header_values[3],
    "packetversion": header_values[4],
    "packet_ID": header_values[5],
    "Session_UID": header_values[6],
    "timestamp": header_values[7],
    "frameIdentifier": header_values[8],
    "value2": header_values[9],
    "playerCarIndex": header_values[10],
    "secondaryPlayerCarIndex": header_values[11],
}

    print(list(data))
    print (header)

