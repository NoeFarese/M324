import requests

url = "https://ifconfig.me"


def get_ip():
    response = requests.get(url)

    if response.status_code == 200:
        print(f"IP: {response.text}")
    else:
        print(f"Error: {response.status_code}")


get_ip()
