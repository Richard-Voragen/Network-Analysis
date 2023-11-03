import dpkt
import socket


def readProtocolsAndHTTP(file):
    print(("_" * 50) + "\nREADING PROTOCOLS AND HTTPS ON:", file, "\n" + ("_" * 50))
    f = open(file, 'rb')
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

    print("Different Application Level Protocols:", dict)
    print("Http Requests: ", httpReq, " Http Responses: ", httpRes, " Https Requests: ", httpsReq, "Https Responses: ", httpsRes)

readProtocolsAndHTTP("Part1.pcap")
readProtocolsAndHTTP("Part2.pcap")
readProtocolsAndHTTP("Part3.pcap")
readProtocolsAndHTTP("Part4.pcap")
readProtocolsAndHTTP("Part5.pcap")
