import requests

def create_session():
    s = requests.Session()
    s.auth = ('user', 'pass')
    s.headers.update({'Student-Id': '918630041'})
    return s

def send_request(session, url, proxies=None, headers=None):
    try:
        response = session.get(url, proxies=proxies, headers=headers, verify=False)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None

def main():
    # Load configuration from a file or environment variables
    url = 'https://kartik-labeling-cvpr-0ed3099180c2.herokuapp.com/ecs152a_ass1'
    proxy = "http://localhost:9000"
    headers = {'Student-Id': '918630041'}

    with create_session() as session:
        # Make requests with or without a proxy
        response_without_proxy = send_request(session, url, headers=headers)
        response_with_proxy = send_request(session, url, proxies={'http': proxy, 'https': proxy}, headers=headers)

    if response_without_proxy:
        print("_" * 50 + "\nRESPONSE WITHOUT PROXY", "\n" + ("_" * 50))
        print(response_without_proxy.headers)

    if response_with_proxy:
        print("_" * 50 + "\nRESPONSE WITH PROXY", "\n" + ("_" * 50))
        print(response_with_proxy.headers)

if __name__ == "__main__":
    main()