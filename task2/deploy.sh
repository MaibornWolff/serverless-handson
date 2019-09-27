#!/bin/bash -e

cd code
serverless deploy -v

echo -e "\n_________________________________\n"
echo -e "\e[33m\e[4mEndpoints:\e[0m"
sls info| grep  GET

cd - > /dev/null