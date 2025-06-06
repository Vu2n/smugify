import requests

def get(url, **kwargs):
    try:
        return requests.get(url, **kwargs).json()
    except Exception as e:
        print(f"❌ GET failed: {e}")
        return None

def post(url, data=None, json=None, **kwargs):
    try:
        return requests.post(url, data=data, json=json, **kwargs).json()
    except Exception as e:
        print(f"❌ POST failed: {e}")
        return None
