import dpkt

f = open("ass1_1.pcap", 'rb')
pcap = dpkt.pcap.Reader(f)