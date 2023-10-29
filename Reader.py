import dpkt

f = open("Problem_1/Part1.pcap", 'rb')
pcap = dpkt.pcap.Reader(f)

dict = {}

for timestamp, data in pcap:
    eth = dpkt.ethernet.Ethernet(data)

    ip = eth.data
    tcp = ip.data

    try:
        name = ip.get_proto(ip.p).__name__
        dict[name] = dict[name] + 1
    except KeyError:
        dict[name] = 1
    except:
        pass



    """ if tcp.dport == 80:
        try:
            http = dpkt.http.Request(tcp.data)
            print(http.headers)
        except:
            pass """
    
print(dict)