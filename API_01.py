import requests
import json
print(f"version of request is {requests.__version__}")

url = "https://uselessfacts.jsph.pl/random.json?language=en"

try:
    response = requests.get(url)
    response.raise_for_status()
    # print(f"status is{response.raise_for_status()} ")
    data = response.json()
    print(data)


except requests.exceptions.RequestException as e:
    print(e)
