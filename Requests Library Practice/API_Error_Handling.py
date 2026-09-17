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

# Handling Errors with try-except

try:
    response=requests.get(url,timeout=10)
    response.raise_for_status()
    print(response.json())

except requests.exceptions.HTTPError as error:
    print('Error Occurred: ',error)


