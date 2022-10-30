import requests
import json

customerId = '1'
apiKey = '8d69bd8d612cfb333618e9e27c59153d'

url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
payload = {
  "type": "Savings",
  "nickname": "test",
  "rewards": 10000,
  "balance": 10000,
}
# Create a Savings Account
response = requests.post(
	url,
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

check = requests.get('http://api.reimaginebanking.com/customers/{}/accounts?key={}')


if response.status_code == 200:
	print('account created')