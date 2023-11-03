import requests

print("Hi")

s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'Student-Id': '918630041'})

# both 'x-test' and 'x-test2' are sent
proxy = "http://localhost:8080"
output = s.get('http://httpbin.org/headers', proxies={'http': proxy, 'https': proxy}, headers={'Student-Id': '918630041'})

print(output.headers)