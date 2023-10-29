import dpkt

f = open("test.pcap", 'rb')
pcap = dpkt.pcap.Reader(f)

for timestamp, data in pcap:
    eth = dpkt.ethernet.Ethernet(data)

    ip = eth.data

    tcp = ip.data

    print(ip.get_proto(ip.p).__name__)

    """ if tcp.dport == 80:
        try:
            http = dpkt.http.Request(tcp.data)
            print(http.headers)
        except:
            pass """