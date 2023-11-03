import dpkt
import socket

def process_pcap_file(file):
    print("_" * 50)
    print(f"READING IPS AND TIMESTAMPS ON: {file}")
    print("_" * 50)
    
    try:
        with open(file, 'rb') as f:
            pcap = dpkt.pcap.Reader(f)

            for timestamp, data in pcap:
                eth = dpkt.ethernet.Ethernet(data)
                ip = eth.data
                tcp = ip.data

                try:
                    destination_ip = socket.inet_ntoa(ip.dst)
                    print(f"Destination IP Address: {destination_ip}\tTimestamp: {timestamp}")
                except socket.error:
                    pass

    except FileNotFoundError:
        print(f"File '{file}' not found.")
    except dpkt.dpkt.NeedData:
        print(f"Failed to read data from '{file}'.")

# List of PCAP files to process
pcap_files = ["Part1.pcap", "Part2.pcap", "Part3.pcap", "Part4.pcap", "Part5.pcap"]

for file in pcap_files:
    process_pcap_file(file)
