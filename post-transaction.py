#! /usr/local/bin/python3

import json
import requests
import os

access_token = os.getenv('ACCESS_TOKEN')
budget_id = os.getenv('BUDGET_ID')
account_id = os.getenv('ACCOUNT_ID')
category_id = os.getenv('CATEGORY_ID')

with open('transaction.json') as transaction_file:
    transaction = json.load(transaction_file)
    transaction['transaction']['account_id'] = account_id
    transaction['transaction']['date'] = "2023-01-01"
    transaction['transaction']['amount'] = 100000
    transaction['transaction']['category_id'] = category_id

    print(json.dumps(transaction))

    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.post(
        url=f"https://api.youneedabudget.com/v1/budgets/{budget_id}/transactions",
        headers=headers,
        json=transaction
    )

    print(response.text)