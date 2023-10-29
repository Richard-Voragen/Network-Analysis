import dpkt

f = open("ass1_1.pcap", 'rb')
pcap = dpkt.pcap.Reader(f)

dict = {}
httpReq = 0
httpRes = 0
httpsReq = 0
httpsRes = 0

for timestamp, data in pcap:
    eth = dpkt.ethernet.Ethernet(data)

    ip = eth.data
    tcp = ip.data

    name = ""
    try:
        name = ip.get_proto(ip.p).__name__
        dict[name] = dict[name] + 1
    except KeyError:
        dict[name] = 1
    except:
        pass

    if name == "TCP":
        if tcp.dport == 80:
            httpReq += 1
            try:
                httpDat = dpkt.http.Request(tcp.data)
                print (httpDat.headers)
            except:
                pass
        if tcp.sport == 80:
            try:
                httpDat = dpkt.http.Request(tcp.data)
                print (httpDat.headers)
            except:
                pass
            httpsRes += 1
        if tcp.dport == 443:
            try:
                httpDat = dpkt.https.Request(tcp.data)
                print (httpDat.headers)
            except:
                pass
            httpsReq += 1
        if tcp.sport == 443:
            try:
                httpDat = dpkt.https.Request(tcp.data)
                print (httpDat.headers)
            except:
                pass
            httpsRes += 1
        
    
print(dict)
print("Http Requests: ", httpReq, " Http Responses: ", httpRes, " Https Requests: ", httpsReq, "Https Responses: ", httpsRes)
