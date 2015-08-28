import requests

def get_rss_json(rss_address):
    r = requests.get(rss_address)
    if r.status_code != 200:
        raise Exception("Could not fetch RSS")
    return r.json()
