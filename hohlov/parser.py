import requests
link = "https://icanhazip.com/"
responce = requests.get(link).text
print(responce)
8