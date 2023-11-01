import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5500

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket: # create socket object
    for message_id in range(1,101):
        message = b'P' * 1000 # send exactly 100 kilobytes of data, assuming 1kb = 1000 bytes
        client_socket.sendto(message, (SERVER_HOST, SERVER_PORT))

        throughput, _ = client_socket.recvfrom(1024)
        print(str(throughput)[2:-1], "kilobytes / second")