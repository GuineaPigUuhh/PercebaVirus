has = True

try:
    import requests
    requests.get("https://www.google.com")
    has = True
except Exception as e:
    has = False