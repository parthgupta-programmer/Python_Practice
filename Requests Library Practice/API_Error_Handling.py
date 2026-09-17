import requests

url=''

response=requests.get(url,timeout=10)


# Checking Status Code Manually

if response.status_code==200:
    print('Request Successful')
    print(response.json())

else:
    print('Request Failed')
    print('Status Code: ',response.status_code)
    print('Response: ',response.text)


