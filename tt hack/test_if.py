# This is written for PYTON 3
# Don't forget to install requests package

import requests
import json
import random

from main import accountId, todays_purchases, last_months_purchases

apiKey = '30e9aa4cdc83efa6616783ed0a2e1b8e'

#get all purchases
get_all_purchases_url = 'http://api.nessieisreal.com/accounts/{}/purchases?key={}'.format(accountId, apiKey)

get_all_purchases_response = requests.get(get_all_purchases_url, accountId)

print("success: ", get_all_purchases_response.content)

