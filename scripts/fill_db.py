import requests

URL = "http://127.0.0.1:8000/rock-groups"

groups = [
    {"name": "Metallica", "country": "USA"},
    {"name": "AC/DC", "country": "Australia"},
    {"name": "Pink Floyd", "country": "UK"},
    {"name": "Rammstein", "country": "Germany"},
    {"name": "Queen", "country": "UK"},
    {"name": "Kiss", "country": "USA"},
    {"name": "The Beatles", "country": "UK"},
    {"name": "Deep Purple", "country": "UK"},
    {"name": "Linkin Park", "country": "USA"},
    {"name": "Scorpions", "country": "Germany"}
]

for group in groups:
    r = requests.post(URL, json=group)
    print(r.status_code, r.json())
