import requests 
r = requests.get('https://www.netflix.com/in/') 
print(r.text) 

with open('r.html', 'w') as f: 
    f.write(r.text)

