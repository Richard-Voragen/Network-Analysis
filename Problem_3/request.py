import requests

print("Hi")

s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'Student-Id': '9186380041'})

# both 'x-test' and 'x-test2' are sent
s.get('http://httpbin.org/headers', headers={'Student-Id': '9186380041'})