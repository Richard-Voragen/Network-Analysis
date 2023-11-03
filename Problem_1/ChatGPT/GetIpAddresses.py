import dpkt
import socket
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name)

def process_pcap_file(file):
    logger.info("_" * 50)
    logger.info(f"READING IPS AND TIMESTAMPS ON: {file}")
    logger.info("_" * 50)
    
    try:
        with open(file, 'rb') as f:
            pcap = dpkt.pcap.Reader(f)

            for timestamp, data in pcap:
                eth = dpkt.ethernet.Ethernet(data)
                ip = eth.data
                tcp = ip.data

                try:
                    destination_ip = socket.inet_ntoa(ip.dst)
                    logger.info(f"Destination IP Address: {destination_ip}\tTimestamp: {timestamp}")
                except socket.error:
                    pass

    except FileNotFoundError:
        logger.error(f"File '{file}' not found.")
    except dpkt.dpkt.NeedData:
        logger.error(f"Failed to read data from '{file}'")
    except:
        pass

def main():
    # List of PCAP files to process
    pcap_files = ["Part1.pcap", "Part2.pcap", "Part3.pcap", "Part4.pcap", "Part5.pcap"]

    for file in pcap_files:
        process_pcap_file(file)

if __name__ == "__main__":
    main()
