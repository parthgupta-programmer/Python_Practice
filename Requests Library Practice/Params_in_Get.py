import requests

params={
    'page':'1',
    'limit':'10'
}

url='https://api.freeapi.app/api/v1/public/randomusers'
response=requests.get(url,params=params,timeout=10)

print(response.json())
print(response.status_code)
