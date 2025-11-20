import requests
import numpy as np


url = "https://icanhazdadjoke.com/"
headers = {'Accept': 'text/plain'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Dad Joke:", response.text)
else:
    print("oh oh... failed to fetch dad joke!")


a = np.array([1, 2, 3])
print(a * 2)
