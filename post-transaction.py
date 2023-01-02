#! /usr/local/bin/python3

import json
import requests
import os

access_token = os.getenv('ACCESS_TOKEN')
print(access_token)


#https://api.youneedabudget.com/v1/budgets/${BUDGET_ID}/transactions
