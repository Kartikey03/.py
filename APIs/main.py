import requests

api_url = "https://api.example.com/data"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    print("API Response:")
    print(data)  

    for item in data["items"]:
        print(f"Item name: {item['name']}, ID: {item['id']}")
else:
    print("Error:", response.status_code)
