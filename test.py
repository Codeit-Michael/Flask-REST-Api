import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + 'helloworld/1',{'name':'Michael','age': 18}) # request = argument
print(response.json())

# input()	# to stop the file reading for a while

# response = requests.get(BASE + 'helloworld/Michael')
# print(response.json())

# input()

# response = requests.put(BASE + 'helloworld/Michael',{'age': 18,'greet':'hello'}) # request = argument
# print(response.json())

# input()
# response = requests.delete(BASE + 'helloworld/Michael')
# print(response)