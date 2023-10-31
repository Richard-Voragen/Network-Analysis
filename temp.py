import dpkt
import socket


def RunAnalysis():
    f = open("ass1_3.pcap", 'rb')
    pcap = dpkt.pcap.Reader(f)

    count = 0
    strs = ["" for x in range(33)]

    for timestamp, data in pcap:
        count += 1
        eth = dpkt.ethernet.Ethernet(data)

        ip = eth.data
        strs[count] = count.__str__() + ", " + socket.inet_ntoa(ip.src).__str__() + ", " + socket.inet_ntoa(ip.dst)

    f.close()

    f = open("ass1_2.pcap", 'rb')
    pcap = dpkt.pcap.Reader(f)

    count = 0

    for timestamp, data in pcap:
        count += 1
        eth = dpkt.ethernet.Ethernet(data)

        ip = eth.data
        print(count.__str__() + ", " + socket.inet_ntoa(ip.src).__str__() + ", " + socket.inet_ntoa(ip.dst) + " & " + strs[count] + " \\\\")
    
    f.close()

RunAnalysis()
