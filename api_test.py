import os
import requests

api_key = os.getenv("MY_API_KEY")

url = "https://httpbin.org/headers"

headers = {
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())