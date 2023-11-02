import dpkt


def findHttpHeaders(file):
    print(("_" * 50) + "\nFINDING SECRETS ON:", file, "\n" + ("_" * 50))
    f = open(file, 'rb')
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
                    
                    secret_line = httpDat.__str__()[httpDat.__str__().find("secret"):]
                    secret = secret_line[:secret_line.find("\n")]
                    print("Packet:", count, "\t", secret)
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
                    httpDat = dpkt.http.Request(tcp.data)
                    print (httpDat.headers)
                except:
                    pass
            if tcp.sport == 443:
                try:
                    httpDat = dpkt.http.Request(tcp.data)
                    print (httpDat.headers)
                except:
                    pass        

findHttpHeaders("ass1_1.pcap")