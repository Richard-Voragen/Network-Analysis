import requests

print("Hi")

login = {'Student-Id', '918630041'}

r = requests.get('https://kartik-labeling-cvpr-0ed3099180c2.herokuapp.com/ecs152a_ass1', headers=login)