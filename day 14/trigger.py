import requests

ngork_url='https//'''''''''.ngrok.io'
endpoint=f'{ngork_url}/box_scraper'

r=requests.post(endpoint,json={})
print(r.json()['data'])