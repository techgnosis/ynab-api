#! /usr/bin/env zsh

set -euo pipefail

curl \
-H "Authorization: Bearer ${ACCESS_TOKEN}" \
https://api.youneedabudget.com/v1/budgets/${BUDGET_ID}/categories | xq