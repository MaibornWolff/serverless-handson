#!/bin/bash -e

cd code
serverless deploy -v

clear
echo -e "\n_________________________________\n"
echo -e "\e[33m\e[4mEndpoints:\e[0m"
sls info| grep  GET

echo -e "\n_________________________________\n"
echo -e "\e[33m\e[4mAWS Web Console Login:\e[0m"
AWS_ACCOUNT=$(aws iam list-users | cut -d ':' -f5)
echo -e "  URL:     https://cloud-school-${AWS_ACCOUNT}-account.signin.aws.amazon.com/console/"

echo "  User:     ${AWS_ACCOUNT}"
echo "  Password: 45%sPmyVpuEttz"

cd - > /dev/null