import dpkt
import socket

# test change

f = open("Problem_1/Part5.pcap", 'rb')
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
        if tcp.sport == 80:
            httpsRes += 1
        if tcp.dport == 443:
            httpsReq += 1
        if tcp.sport == 443:
            httpsRes += 1

    name = socket.inet_ntoa(ip.dst).__str__()
    print("Destination IP Address: " + name + " \tTimestamp: " + timestamp.__str__())

    

print(dict)
print("Http Requests: ", httpReq, " Http Responses: ", httpRes, " Https Requests: ", httpsReq, "Https Responses: ", httpsRes)
