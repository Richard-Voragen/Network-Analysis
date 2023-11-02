import socket
import time

HOST = '127.0.0.1' # local machine IP address
PORT = 5500

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket: # specify UDP socket, store as server_socket
    server_socket.bind((HOST, PORT)) # bind socket object

    initial_time = time.time() # issues: have client pass this value to server?
    total_data = 0

    while True:
        data, addr = server_socket.recvfrom(1024) # infinitely receive data from client, 1024 bytes of data received each time
        print(f"Received {data.decode()} from {addr}")

        total_data += len(data)
        print(total_data, "bytes received")

        if total_data == 100000:
            print("Data limit reached")
            final_time = time.time()
            throughput = (total_data / 1024) / (final_time - initial_time)

            throughput_converted = str(throughput).encode()
            server_socket.sendto(throughput_converted, addr)
        else:
            server_socket.sendto(b'Z', addr)