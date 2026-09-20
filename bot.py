import requests

URL = "https://trouverunlogement.lescrous.fr/"

response = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=20
)

print("Code HTTP :", response.status_code)

if response.status_code == 200:
    print("✅ Le bot arrive bien à contacter le site CROUS")
else:
    print("❌ Problème pour contacter le site CROUS")
