#! /usr/bin/env bash

set -euo pipefail

curl \
-H "Authorization: Bearer ${ACCESS_TOKEN}" \
https://api.youneedabudget.com/v1/budgets | xq