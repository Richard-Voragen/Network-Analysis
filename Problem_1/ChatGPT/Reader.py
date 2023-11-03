import dpkt
import socket
from collections import defaultdict

HTTP_PORT = 80
HTTPS_PORT = 443

def readProtocolsAndHTTP(file):
    print(("_" * 50) + f"\nREADING PROTOCOLS AND HTTPS ON: {file}\n" + ("_" * 50))

    with open(file, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)

        protocol_count = defaultdict(int)
        http_req = 0
        http_res = 0
        https_req = 0
        https_res = 0

        for timestamp, data in pcap:
            eth = dpkt.ethernet.Ethernet(data)

            ip = eth.data
            tcp = ip.data

            try:
                protocol_name = ip.get_proto(ip.p).__name__
                protocol_count[protocol_name] += 1
            except:
                pass

            if protocol_name == "TCP":
                if tcp.dport == HTTP_PORT:
                    http_req += 1
                if tcp.sport == HTTP_PORT:
                    http_res += 1
                if tcp.dport == HTTPS_PORT:
                    https_req += 1
                if tcp.sport == HTTPS_PORT:
                    https_res += 1

        print("Different Application Level Protocols:", dict(protocol_count))
        print(f"Http Requests: {http_req}, Http Responses: {http_res}, Https Requests: {https_req}, Https Responses: {https_res}")

if __name__ == "__main__":
    pcap_files = ["Part1.pcap", "Part2.pcap", "Part3.pcap", "Part4.pcap", "Part5.pcap"]
    for file in pcap_files:
        readProtocolsAndHTTP(file)