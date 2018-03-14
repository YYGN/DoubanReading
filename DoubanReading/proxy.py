import requests

from .settings import REDIS_URI, REDIS_PORT, REDIS_PWD

proxy_url = 'http://0.0.0.1:5555'

def get_proxy():
    try:
        response = requests.get(proxy_url)
        response.raise_for_status()
        return response.text
    except:
        return None