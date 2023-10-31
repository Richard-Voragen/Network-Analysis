import dpkt

f = open("ass1_1.pcap", 'rb')
pcap = dpkt.pcap.Reader(f)

count = 0

for timestamp, data in pcap:
    count += 1
    eth = dpkt.ethernet.Ethernet(data)

    ip = eth.data
    tcp = ip.data

    name = ""
    name = ip.get_proto(ip.p).__name__


    if name == "TCP":
        if tcp.dport == 80:
            try:
                httpDat = dpkt.http.Request(tcp.data)
                
                print("On transmission: ", count, " The client sent the server: ", tcp.__str__()[tcp.__str__().rfind('\\x')+4:])
            except:
                pass
        if tcp.sport == 80:
            try:
                httpDat = dpkt.http.Request(tcp.data)
                print (httpDat.headers)
            except:
                pass
        if tcp.dport == 443:
            try:
                httpDat = dpkt.https.Request(tcp.data)
                print (httpDat.headers)
            except:
                pass
        if tcp.sport == 443:
            try:
                httpDat = dpkt.https.Request(tcp.data)
                print (httpDat.headers)
            except:
                pass        