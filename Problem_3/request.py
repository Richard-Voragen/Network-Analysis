import requests

print("Hi")

s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'Student-Id': '918630041'})

# both 'x-test' and 'x-test2' are sent
proxy = "http://localhost:9000"
output = requests.get('https://kartik-labeling-cvpr-0ed3099180c2.herokuapp.com/ecs152a_ass1', proxies={'http': proxy, 'https': proxy}, headers={'Student-Id': '918630041'})

print(output.headers)