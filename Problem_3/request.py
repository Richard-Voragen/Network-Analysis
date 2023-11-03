import requests

print("Hi")

s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'Student-Id': '918630041'})

# response with no proxy
print(("_" * 50) + "\nRESPONSE WITHOUT PROXY", "\n" + ("_" * 50))
output = requests.get('https://kartik-labeling-cvpr-0ed3099180c2.herokuapp.com/ecs152a_ass1', headers={'Student-Id': '918630041'}, verify=False)
print(output.headers)
""" 
# response with proxy
print(("_" * 50) + "\nRESPONSE WITH PROXY", "\n" + ("_" * 50))
proxy = "http://localhost:9000"
output = requests.get('https://kartik-labeling-cvpr-0ed3099180c2.herokuapp.com/ecs152a_ass1', proxies={'http': proxy, 'https': proxy}, headers={'Student-Id': '918630041'}, verify=False)
print(output.headers) """