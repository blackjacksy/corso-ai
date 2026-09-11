import requests

risposta = requests.get("https://www.google.com")

print(risposta.status_code)