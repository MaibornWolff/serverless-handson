#!/bin/bash -e

cd code
serverless deploy -v

clear
echo -e "\n_________________________________\n"
echo -e "\e[33m\e[4mEndpoints:\e[0m"
sls info| grep  GET

echo -e "\n_________________________________\n"
echo -e "\e[33m\e[4mAWS Console Login:\e[0m"
AWS_ACCOUNT=$(aws iam list-users  --output text | cut -d ':' -f5)
echo -e " url: https://${AWS_ACCOUNT}.signin.aws.amazon.com/console/"





cd - > /dev/null