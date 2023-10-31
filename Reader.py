import dpkt
import socket

f = open("Problem_1/Part5.pcap", 'rb')
pcap = dpkt.pcap.Reader(f)

dict = {}
ips = {}
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

    name = ""
    try:
        name = socket.inet_ntoa(ip.dst).__str__()
        ips[name] = ips[name] + " " + timestamp.__str__()
    except KeyError:
        ips[name] = timestamp.__str__()
    except:
        pass
        
for time in ips:
    splitted = ips[time].split(' ')
    iterator = 3
    try:
        print("& " + time + " & " + splitted[0] + ", " + splitted[1] + ", " + splitted[2] + ", \\\\")
    except:
        try: 
            print("& " + time + " & " + splitted[0] + ", " + splitted[1] + ", \\\\")
        except:
            print("& " + time + " & " + splitted[0] + " \\\\")
    while (iterator < len(splitted)):
        try:
            print("& & " + splitted[iterator] + ", " + splitted[iterator+1] + ", " + splitted[iterator+2] + ", \\\\")
        except:
            try: 
                print("& & " + splitted[iterator] + ", " + splitted[iterator+1] + ", \\\\")
            except:
                print("& & " + splitted[iterator] + " \\\\")
        iterator += 3
    print ("\cline{2-3}")

    

print(dict)
print("Http Requests: ", httpReq, " Http Responses: ", httpRes, " Https Requests: ", httpsReq, "Https Responses: ", httpsRes)
