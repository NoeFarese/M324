import requests
import numpy as np


url = "https://icanhazdadjoke.com/"
headers = {'Accept': 'text/plain'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    joke = response.text
    print("Joke:", joke)
else:
    print("Failed to fetch joke. Status code:", response.status_code)


a = np.array([1, 2, 3])
print(a * 2)
