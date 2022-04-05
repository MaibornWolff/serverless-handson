#!/bin/bash
#npm install -g yarn serverless
#sudo yum -y install jq
#sudo easy_install-3.6 pip
#sudo pip-3.6 install requests requests-toolbelt

cd task1/src && npm init -y && npm install --save serverless-python-requirements

# extracts the group ID from the AWS user name, e.g. cs12 would result in 12
#echo -e "\n\nexport GROUP_ID=${C9_USER#'cs'}" >> ~/.bashrc
