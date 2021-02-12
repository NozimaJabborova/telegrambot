import requests 
import json
from pprint import pprint
token='1656085440:AAFz1LuUJC6hL4tk_NVC8shyw0ArnQ1ET9g'
url=f'https://api.telegram.org/bot{token}/getMe'
r=requests.get(url)
#print(r.url)
#data=r.json()
user=r.json()
pprint(user)