import requests 
# r = requests.post('https://httpbin.org/post', data={'key': 'value'}) 

r = requests.put('https://httpbin.org/put', data={'key': 'value', 'key2': 'value2'})

print(r.text) 
# print(r.json()['url']) 
# print(r.url) 
