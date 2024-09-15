import requests 
http_proxy = 'http://38.154.227.167:5868:ltpmarlw:1rc4vsbiqi0n'
https_proxy = 'http://38.154.227.167:5868:ltpmarlw:1rc4vsbiqi0n'

proxies = {
    'http' : http_proxy, 
    'https' : https_proxy 
}

r = requests.get('https://httpbin.org/get', proxies=proxies) 

print(r.text) 

