import socket
import time

# *** current issues - calculation of initial time ***
# initial time should be sent from client to server?
# current implementation - initial time within 'while True' returns ZeroDivisionError, initial time outside 'while True' results in very low values

HOST = '127.0.0.1' # local machine IP address
PORT = 5500

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket: # specify UDP socket, store as server_socket
    server_socket.bind((HOST, PORT)) # bind socket object

    initial_time = time.time() # issues: have client pass this value to server?
    
    while True:
        data, addr = server_socket.recvfrom(1024) # infinitely receive data from client, 1024 bytes of data received each time
        print(f"Received {data.decode()} from {addr}")

        final_time = time.time()

        throughput = (len(data) / 1024) / (final_time - initial_time)

        # try:
        #     throughput = (len(data) / 1024) / (final_time - initial_time)
        # except ZeroDivisionError:
        #     throughput = 0

        print("Final =", final_time, "Initial =", initial_time, "Throughput =", throughput)

        throughput_converted = str(throughput).encode()
        server_socket.sendto(throughput_converted, addr)