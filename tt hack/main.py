

# This is written for PYTHON 3
# Don't forget to install requests package

import requests
import json
import random

apiKey = '30e9aa4cdc83efa6616783ed0a2e1b8e'
merchant_ids = []
todays_date = "2022-10-30"
last_months_date = "2022-9-30"
todays_purchases = 0
last_months_purchases = 0

create_customer_url = 'http://api.nessieisreal.com/customers?key={}'.format(apiKey)
customer_payload = {
  "first_name": "John",
  "last_name": "Smith",
  "address": {
     "street_number": "100",
     "street_name": "Commonwealth Ave",
     "city": "Boston",
     "state": "MA",
     "zip": "02115"
  }
}
# Create a customer
response = requests.post(
  create_customer_url,
  data=json.dumps(customer_payload),
  headers={'content-type':'application/json'},
)

loaded = json.loads(response.text)
# Loop along dictionary keys
for iterator in loaded:
  if (iterator == "objectCreated"):
     customerId = (loaded[iterator]["_id"])

create_account_url = 'http://api.nessieisreal.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
create_account_payload = {
 "type": "Credit Card",
 "nickname": "My Credit",
 "rewards": 0,
 "balance": 0,
}
# Create a credit account
response1 = requests.post(
  create_account_url,
  data=json.dumps(create_account_payload),
  headers={'content-type':'application/json'}
)

# Get info
get_account_url = 'http://api.nessieisreal.com/customers/{}/accounts?key={}'.format(customerId, apiKey)

response2 = requests.get(get_account_url, customerId)

print(response2.content)
loaded2 = json.loads(response2.text)
accountId = (loaded2[0]["_id"])

# Create merchants
create_merchant_url = 'http://api.nessieisreal.com/merchants?key={}'.format(apiKey)
for i in range(15):
  create_merchant_payload = {
    "name": "Merchant" + str(i + 1)
  }

  create_merchant_response = requests.post(
  create_merchant_url,
  data=json.dumps(create_merchant_payload),
  headers={'content-type':'application/json'})

  loaded3 = json.loads(create_merchant_response.text)
  # Loop along dictionary keys
  for iterator in loaded3:
     if (iterator == "objectCreated"):
        merchant_ids.append(loaded3[iterator]["_id"])

# Add purchases
# Create purchase url
create_purchase_url = 'http://api.nessieisreal.com/accounts/{}/purchases?key={}'.format(accountId, apiKey)
# make purchases for August
for i in range(10):
  create_purchase_payload = {
    "merchant_id": merchant_ids[random.randrange(0, 15)],
    "medium": "balance",
    "purchase_date": "2022-8-" + str(random.randrange(1, 32)),
    "amount": round(random.random() * 30, 2),
    "status": "completed"
  }

  create_purchase_response = requests.post(
     create_purchase_url,
     data=json.dumps(create_purchase_payload),
     headers={'content-type':'application/json'})
# make purchases for September
for i in range(10):
  create_purchase_payload = {
    "merchant_id": merchant_ids[random.randrange(0, 15)],
    "medium": "balance",
    "purchase_date": "2022-9-" + str(random.randrange(1, 31)),
    "amount": round(random.random() * 30, 2),
    "status": "completed"
  }

  create_purchase_response = requests.post(
     create_purchase_url,
     data=json.dumps(create_purchase_payload),
     headers={'content-type':'application/json'})
# make purchases for October
for i in range(10):
  create_purchase_payload = {
    "merchant_id": merchant_ids[random.randrange(0, 15)],
    "medium": "balance",
    "purchase_date": "2022-10-" + str(random.randrange(1, 32)),
    "amount": round(random.random() * 30, 2),
    "status": "completed"
  }

  create_purchase_response = requests.post(
     create_purchase_url,
     data=json.dumps(create_purchase_payload),
     headers={'content-type':'application/json'})
# ensure purchase for October 30, 2022
create_purchase_payload = {
 "merchant_id": merchant_ids[random.randrange(0, 15)],
 "medium": "balance",
 "purchase_date": "2022-10-30",
 "amount": round(random.random() * 30, 2),
 "status": "completed"
}
create_purchase_response = requests.post(
  create_purchase_url,
  data=json.dumps(create_purchase_payload),
  headers={'content-type': 'application/json'})
# ensure purchase for last month's same date
create_purchase_payload = {
 "merchant_id": merchant_ids[random.randrange(0, 15)],
 "medium": "balance",
 "purchase_date": "2022-9-30",
 "amount": round(random.random() * 30, 2),
 "status": "completed"
}
create_purchase_response = requests.post(
  create_purchase_url,
  data=json.dumps(create_purchase_payload),
  headers={'content-type': 'application/json'})

#get all purchases
get_all_purchases_url = 'http://api.nessieisreal.com/accounts/{}/purchases?key={}'.format(accountId, apiKey)

get_all_purchases_response = requests.get(get_all_purchases_url, accountId)

all_purchases = json.loads(get_all_purchases_response.text)
# Loop thru all purchases
for purchase_num, purchase in enumerate(all_purchases):
  if (purchase["purchase_date"] == todays_date):
     todays_purchases += all_purchases[purchase_num]['amount']
  elif (purchase["purchase_date"] == last_months_date):
     last_months_purchases += all_purchases[purchase_num]['amount']



