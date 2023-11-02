import socket
import time

HOST = '127.0.0.1'
PORT = 5500
DATA_LIMIT_BYTES = 100000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))
    initial_time = time.time()
    total_data = 0

    while True:
        data, addr = server_socket.recvfrom(1024)
        total_data += len(data)
        print(f"Received {len(data)} bytes from {addr}, Total: {total_data} bytes")

        if total_data >= DATA_LIMIT_BYTES:
            print("Data limit reached")
            final_time = time.time()
            throughput = (total_data / 1024) / (final_time - initial_time)
            throughput_converted = str(throughput).encode()
            server_socket.sendto(throughput_converted, addr)
            break

        server_socket.sendto(b'Z', addr)