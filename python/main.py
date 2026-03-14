from listen import create_socket
from parser import parse_header
import struct

sock = create_socket()

while True:
    data, addr = sock.recvfrom(2048) # F1 packets vary in size
   # print(list(data))


    header = parse_header(data)

    # different packet types based of TimeTrail 
    match header["packet_ID"]:
      case 0: #Motion packet. Car  movement when player is in control 
        pass #TODO 
      case 1: # Session packets 
        pass #TODO 
      case 2: # Lap Data packets
        pass #TODO
      case 3: #Event packets. specific events in the game like start of session, fastest lap, retirement etc
        print("hello there. this is an event packet. not much to see here yet")
      case 11: # Session History packetes. Lap and tyre data for the session.
        pass #TODO 
      case 12: #Tyrpe set packet. Tyre data for the session.
        pass #TODO
      case 13:  #Motion Ex. 
        pass #TODO
      case 14: #TimeTrail packets,
        pass #TODO
      
          
    print (header)
    print ("packetID:", packetID := header["packet_ID"])



          
    

  # print("size:", header_size)
    #motion packets 


