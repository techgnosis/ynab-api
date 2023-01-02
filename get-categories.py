#! /usr/local/bin/python3

import requests
import os
import json


access_token = os.getenv("ACCESS_TOKEN")
budget_id = os.getenv("BUDGET_ID")

headers = {"Authorization": f"Bearer {access_token}"}

response = requests.get(
    url=f"https://api.youneedabudget.com/v1/budgets/{budget_id}/categories",
    headers=headers
    )

print(json.dumps(response.json(), indent=2))