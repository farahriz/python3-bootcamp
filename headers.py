import requests

url = "https://icanhazdadjoke.com"

response1 = requests.get(url, headers={"Accept": "text/plain"})
response2 = requests.get(url, headers={"Accept": "application/json"})

data = response2.json()

print(response1.text)
print(data)