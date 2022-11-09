import urequests
import ujson

def get_text(url):
    res = urequests.get(url=url)
    return res.text

def get_json(url):
        return ujson.loads(get_text(url))
