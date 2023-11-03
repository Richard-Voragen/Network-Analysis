import dpkt
import socket
import logging

def process_packet(timestamp, data):
    eth = dpkt.ethernet.Ethernet(data)

    # Check if it's an IP packet
    if isinstance(eth.data, dpkt.ip.IP):
        ip = eth.data
        try:
            destination_ip = socket.inet_ntoa(ip.dst)
            return destination_ip, timestamp
        except socket.error:
            return None, None
    # Check if it's an ARP packet
    elif isinstance(eth.data, dpkt.arp.ARP):
        return "ARP Packet", timestamp
    else:
        return None, None

def process_pcap_file(file):
    logging.info("_" * 50)
    logging.info(f"READING IPS AND TIMESTAMPS ON: {file}")
    logging.info("_" * 50)
    
    try:
        with open(file, 'rb') as f:
            pcap = dpkt.pcap.Reader(f)

            for timestamp, data in pcap:
                destination_ip, timestamp = process_packet(timestamp, data)
                if destination_ip is not None:
                    logging.info(f"Destination IP Address: {destination_ip}\tTimestamp: {timestamp}")

    except FileNotFoundError:
        logging.error(f"File '{file}' not found.")
    except dpkt.dpkt.NeedData:
        logging.error(f"Failed to read data from '{file}'")

if __name__ == "__main__":
    # Configure the logger
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    
    # List of PCAP files to process
    pcap_files = ["../Part1.pcap", "../Part2.pcap", "../Part3.pcap", "../Part4.pcap", "../Part5.pcap"]

    for file in pcap_files:
        process_pcap_file(file)
