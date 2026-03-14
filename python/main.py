from listen import create_socket

sock = create_socket()

while True:
    data, addr = sock.recvfrom(2048)  # F1 packets vary in size
    print(f"Received {data} bytes from {addr}")