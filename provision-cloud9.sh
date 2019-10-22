#!/bin/bash
npm install -g yarn serverless
sudo yum -y install jq
sudo easy_install-3.6 pip
sudo pip-3.6 install requests

# extracts the group ID from the AWS user name, e.g. cs12 would result in 12
echo -e "\n\nexport GROUP_ID=${C9_USER#'cs'}" >> ~/.bashrc

while true; do
  echo -n "Enter the IP of the Elasticsearch instance [ENTER]: "
  read -r ELASTIC_IP

  export ELASTIC_IP=$ELASTIC_IP
  export ELASTIC_URL="http://$ELASTIC_IP:9200"

  if curl --output /dev/null --connect-timeout 3 --max-time 6 --silent --head --fail "$ELASTIC_URL"; then
    echo -e "\n\nexport ELASTIC_IP=\"${ELASTIC_IP}\"" >> ~/.bashrc

    echo "Provisioning finished. Please use a new terminal and go on with the README.md"
    break;
  else
    echo "No Elasticsearch instance found under ${ELASTIC_URL}"
  fi
done