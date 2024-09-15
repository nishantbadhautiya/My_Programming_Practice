import requests 

payload = {
    'key1': 'value1', 
    'key2': ['value2', 'value3']
}

r = requests.get('https://httpbin.org/get', params=payload)

print(r.text) 
print(r.encoding) 
r.encoding = 'ISO-8859-1'

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 

data = r.text 
print(data) 
print(r.encoding) 
