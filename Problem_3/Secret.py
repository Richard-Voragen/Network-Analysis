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
        try:
            name = ip.get_proto(ip.p).__name__
        except:
            pass


        if name == "TCP":
            if tcp.dport == 80:
                print("HTTP Request")
                try:
                    httpDat = dpkt.http.Request(tcp.data)
                    print (httpDat.headers)
                except:
                    pass
            if tcp.sport == 80:
                print("HTTP Response")
                try:
                    httpDat = dpkt.http.Request(tcp.data)
                    print (httpDat.headers)
                except:
                    pass
            if tcp.dport == 443:
                print("HTTPS Request")
                try:
                    httpDat = dpkt.http.Request(tcp.data)
                    print (httpDat.headers)
                except:
                    pass
            if tcp.sport == 443:
                print("HTTPS Response")
                try:
                    httpDat = dpkt.http.Request(tcp.data)
                    print (httpDat.headers)
                except:
                    pass        

# findHttpHeaders("BeforeProxy.pcap")
findHttpHeaders("AfterProxy.pcap")