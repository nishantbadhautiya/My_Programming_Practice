import requests 

from PIL import Image

from io import BytesIO

r = requests.get('https://img.freepik.com/free-photo/painting-mountain-lake-with-mountain-background_188544-9126.jpg') 

fp =  open('image.jpg', 'wb')  
i = Image.open(BytesIO(r.content))

i.save(fp) 
fp.close()


