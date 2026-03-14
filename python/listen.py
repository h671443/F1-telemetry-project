import socket

#Define UDP packet and port 


UDP_IP = "192.168.1.251"
UDP_PORT = 20777    # default port used by F1 games

def create_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT)); 
    print(f"Listening on {UDP_IP}:{UDP_PORT}"); 
    return sock
