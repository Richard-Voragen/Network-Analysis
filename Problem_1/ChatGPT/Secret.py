import dpkt

def findHttpHeaders(file_path):
    print("_" * 50)
    print("FINDING SECRETS ON:", file_path)
    print("_" * 50)

    try:
        with open(file_path, 'rb') as f:
            pcap = dpkt.pcap.Reader(f)

            count = 0

            for timestamp, data in pcap:
                count += 1
                eth = dpkt.ethernet.Ethernet(data)

                ip = eth.data
                tcp = ip.data

                name = ip.get_proto(ip.p).__name__

                if name == "TCP":
                    try:
                        http_request = dpkt.http.Request(tcp.data)

                        secret_line = http_request.__str__()[http_request.__str__().find("secret"):]
                        secret = secret_line[:secret_line.find("\n")]
                        print("Packet:", count, "\t", secret)
                    except dpkt.dpkt.NeedData:
                        pass

                if tcp.dport in {80, 443} or tcp.sport in {80, 443}:
                    try:
                        http_request = dpkt.http.Request(tcp.data)
                        print(http_request.headers)
                    except dpkt.dpkt.NeedData:
                        pass

    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    findHttpHeaders("ass1_1.pcap")