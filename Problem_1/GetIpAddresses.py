import dpkt
import socket


def read_IPs_and_timestamps(file):
    print(("_" * 50) + "\nREADING IPS AND TIMESTAMPS ON:", file, "\n" + ("_" * 50))
    f = open(file, 'rb')
    pcap = dpkt.pcap.Reader(f)

    for timestamp, data in pcap:
        eth = dpkt.ethernet.Ethernet(data)

        ip = eth.data
        tcp = ip.data

        try:
            name = socket.inet_ntoa(ip.dst).__str__()
            print("Destination IP Address: " + name + " \tTimestamp: " + timestamp.__str__())
        except:
            pass

read_IPs_and_timestamps("Part1.pcap")
read_IPs_and_timestamps("Part2.pcap")
read_IPs_and_timestamps("Part3.pcap")
read_IPs_and_timestamps("Part4.pcap")
read_IPs_and_timestamps("Part5.pcap")