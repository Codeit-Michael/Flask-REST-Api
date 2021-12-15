import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + 'helloworld/2',{'name':'Michael','age': 21}) # request = argument
print(response.json())

input()	# to stop the file reading for a while

# response = requests.get(BASE + 'helloworld/1',{})
# print(response.json())

# input()

response = requests.patch(BASE + 'helloworld/2',{'name':'Agg'}) # request = argument
print(response.json())

# input()
# response = requests.delete(BASE + 'helloworld/Michael')
# print(response)