#! /usr/bin/env zsh

set -euo pipefail

colima nerdctl run -- \
--rm \
-it \
-v $(pwd):/opt/python \
--env ACCESS_TOKEN=${ACCESS_TOKEN} \
--env BUDGET_ID=${BUDGET_ID} \
--env ACCOUNT_ID=${ACCOUNT_ID} \
python:3.11 bash

