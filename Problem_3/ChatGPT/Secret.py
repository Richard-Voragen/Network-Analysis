import dpkt

def process_http_data(data, protocol):
    try:
        http_request = dpkt.http.Request(data)
        print(f"{protocol} Request Headers:")
        print(http_request.headers)
    except dpkt.dpkt.NeedData:
        pass

def find_http_headers(file_path):
    print("_" * 50)
    print("FINDING SECRETS ON:", file_path)
    print("_" * 50)

    with open(file_path, 'rb') as file:
        pcap = dpkt.pcap.Reader(file)

        for _, packet_data in pcap:
            eth = dpkt.ethernet.Ethernet(packet_data)
            ip = eth.data
            tcp = ip.data
            try:
                protocol = ip.get_proto(ip.p).__name__
            except:
                continue

            if protocol == "TCP":
                if tcp.dport in [80, 443]:
                    if tcp.sport == 80:
                        print("HTTP Response")
                    elif tcp.sport == 443:
                        print("HTTPS Response")
                    elif tcp.dport == 80:
                        print("HTTP Request")
                        process_http_data(tcp.data, "HTTP")
                    elif tcp.dport == 443:
                        print("HTTPS Request")
                        process_http_data(tcp.data, "HTTPS")

if __name__ == "__main__":
    find_http_headers("../test.pcap")
    # find_http_headers("../AfterProxy.pcap")