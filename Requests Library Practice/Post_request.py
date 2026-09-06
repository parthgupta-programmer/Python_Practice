import requests

url = "https://api.freeapi.app/api/v1/kitchen-sink/http-methods/post"

data={
    "name": "Hello",
    "age": 20,
    "course": "AI Engineering"
}

response = requests.post(url, json=data, timeout=10)

print("Status Code:", response.status_code)
print("Response:", response.json())

# Status Code: 200
# Response: {'statusCode': 200, 'data': {'method': 'POST', 'headers': {'connection': 'upgrade', 'host': 'api.freeapi.app', 'x-real-ip': '152.58.117.87', 'x-forwarded-for': '152.58.117.87', 'content-length': '56', 'user-agent': 'python-requests/2.27.1', 'accept-encoding': 'gzip, deflate, br', 'accept': '*/*', 'content-type': 'application/json'}, 'origin': '::ffff:192.168.32.3', 'url': 'http://api.freeapi.app/api/v1/kitchen-sink/http-methods/post'}, 'message': 'POST request', 'success': True}