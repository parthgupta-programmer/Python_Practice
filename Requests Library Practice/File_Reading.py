import requests
from io import BytesIO

url='https://drive.usercontent.google.com/download?id=1M2Atf4iPDMFM3W93WBtg1bK89L1yRlMP&export=download&authuser=0&confirm=t&uuid=b44b2d00-bfb0-4a40-b48e-86e2d50f9ae0&at=AFYLz4OvGiJMvt26wYMNTupkcptZ:1785423888630'

response=requests.get(url)

fp=open("Requests Library Practice/downloaded_file.pdf", "wb")
fp.write(response.content)
fp.close()