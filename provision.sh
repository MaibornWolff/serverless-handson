#!/bin/bash
sudo npm install -g yarn serverless
sudo yum -y install jq
echo -e '\n\nexport GROUP_ID=`cat ~/.aws/credentials | grep aws_access_key_id | cut -d = -f 2 |shasum | head -c 6`' >> ~/.bashrc