import requests

url='https://api.freeapi.app/api/v1/kitchen-sink/http-methods/put'

updated_data={
    "name": "Hello2",
    "age": 22,
    "course": 'Machine Learning'
}

response=requests.put(url, json=updated_data)

print("Status Code:", response.status_code)
print('Response:', response.json())

