import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.get(BASE + 'helloworld/Michael')
response = requests.put(BASE + 'helloworld/Michael',{'subs': 1000})	# the request = argument

print(response.json())