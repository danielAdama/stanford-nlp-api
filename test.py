import requests

url = "http://localhost:8080/v1/process"
resp = requests.post(url, json="I saw the man with the binoculars on the hill.")
print(resp.json())