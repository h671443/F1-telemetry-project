import struct 
#TODO: add parsing class 



def parse_header(data):
    header_values=struct.unpack_from("<HBBBBBQfLLBB", data, 0)
    header_size=struct.calcsize("<HBBBBBQfLLBB")

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
    return header

def parse_payload(data, payload_bytes):
    pass #TODO