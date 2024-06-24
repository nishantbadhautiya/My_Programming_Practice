import requests 

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.get('https://httpbin.org/get', params=payload)
# print(r.text)

print(r.json(), type(r.json())) 

print(r.url) # You can see that the URL has been correctly encoded by printing the URL

