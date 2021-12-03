import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.get(BASE + 'helloworld/Michael')
response = requests.put(BASE + 'helloworld/Michael',{'age': 18,'greet':'hello'}) # request = argument
# response = requests.put(BASE + 'helloworld/Michael',{'age':17})
print(response.json())