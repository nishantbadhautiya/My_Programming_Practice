import requests

links = ['https://www.codewithharry.com/videos', 'https://www.codewithharry.com/blog', 'https://www.codewithharry.com/contact']

for link in links: 
    r = requests.get(link)
    filename = f"htmls/{link.split('/')[-1]}.html"
    with open(filename, 'w') as fp: 
        fp.write(r.text)

print("Files downloaded successfully!")

