import dpkt
import socket

def analyze_pcap(file_path):
    """
    Analyze a PCAP file and count the number of pings and pongs.
    
    Args:
        file_path (str): Path to the PCAP file to analyze.
    """
    print("_" * 50)
    print("RUNNING ANALYSIS ON:", file_path)
    print("_" * 50)

    ping_count = 0
    pong_count = 0

    with open(file_path, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)

        for count, (timestamp, data) in enumerate(pcap, start=1):
            eth = dpkt.ethernet.Ethernet(data)
            ip = eth.data
            src_ip = socket.inet_ntoa(ip.src)
            dst_ip = socket.inet_ntoa(ip.dst)

            if ip.data.endswith(b'\x00' * 24):
                message_type = "ping"
                ping_count += 1
            else:
                message_type = "pong"
                pong_count += 1

            print(f"{count}, {src_ip}, {dst_ip}, {message_type}")

    print("Total Pings:", ping_count, "Total Pongs:", pong_count)

# Call the function with your PCAP file paths
analyze_pcap("../ass1_2.pcap")
analyze_pcap("../ass1_3.pcap")
