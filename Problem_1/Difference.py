import dpkt
import socket


def RunAnalysis(file):
    print(("_" * 50) + "\nRUNNING ANALYSIS ON:", file, "\n" + ("_" * 50))
    f = open(file, 'rb')
    pcap = dpkt.pcap.Reader(f)

    count = 0
    ping = 0
    pong = 0

    for timestamp, data in pcap:
        count += 1
        eth = dpkt.ethernet.Ethernet(data)

        ip = eth.data
        print(count.__str__() + ",", socket.inet_ntoa(ip.src).__str__() + ",", socket.inet_ntoa(ip.dst))
        tcp = ip.data

        if (ip.data.__str__()[-96:] == "x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\'"):
            type = "ping"
            ping += 1
        else:
            type = "pong"
            pong += 1

    print ("Total Pings: ", ping, " Total Pongs: ", pong)
    f.close()

RunAnalysis("ass1_2.pcap")
RunAnalysis("ass1_3.pcap")