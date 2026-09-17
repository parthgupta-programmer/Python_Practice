import requests

url='https://api.freeapi.app/api/v1/public/randomusers/user/random'

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

# Handling Different Errors

try:
    response=requests.get(url,timeout=10)
    response.raise_for_status()
    print(response.json())

except requests.exceptions.Timeout:
    print('The request timed out.')

except requests.exceptions.ConnectionError:
    print('Could not connect to the server.')

except requests.exceptions.JSONDecodeError:
    print('Invalid JSON response.')

except requests.exceptions.RequestException as err:
    print('Request Error: ',err)



