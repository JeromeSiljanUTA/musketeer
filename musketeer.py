import requests
import json
import pandas as pd

url = f'https://api.stockdata.org/v1/data/intraday?'

payload = {
        'symbols': 'TSLA',
        'api_token': 'fAJ618UaqQRCpHDm8mP7PbP2HlR4nhxlyiXGoFJY',
        'date_from': '2020-01-01'
        }

response = requests.get(url, params=payload)

response = response.json()

for entry in response['data']:
    print(f'{entry["date"]}\n')
    break
