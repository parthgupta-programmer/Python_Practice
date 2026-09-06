import requests
from PIL import Image
from io import BytesIO

url = "https://images.unsplash.com/photo-1787894653068-bf1eeb927af4?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

response = requests.get(url)

img = Image.open(BytesIO(response.content))

fp=open("Requests Library Practice/downloaded_image.jpg", "wb")
img.save(fp)
fp.close()

