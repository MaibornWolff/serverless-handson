#!/bin/bash -e

if [[ -z "${GROUP_ID}" ]]; then
    echo "[ERROR] GROUP_ID is not set as environment variable"
    exit 1
fi

cd code
serverless deploy -v


echo -e "\n_________________________________\n"
echo -e "\e[33m\e[4mEndpoints:\e[0m"
sls info| grep  GET

cd - > /dev/null