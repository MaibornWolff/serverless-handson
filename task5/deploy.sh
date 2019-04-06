#!/usr/bin/env bash

set -e
# deploy backend
cd code
yarn install --frozen-lockfile

serverless remove 2>&1 >/dev/null || true  # just in case any stack exists

serverless deploy -v
BASE_URL=`sls info -v | grep ServiceEndpoint: | xargs |cut -d " " -f2`
cd - > /dev/null

mkdir frontend/src/environments
echo "export const environment = {
  production: false,
  lambdaApiEndpoint: '${BASE_URL}'
};" > frontend/src/environments/environment.ts

echo "export const environment = {
  production: true,
  lambdaApiEndpoint: '${BASE_URL}'
};" > frontend/src/environments/environment.prod.ts

# build frontend
cd frontend
if [[ $1 == "--build" ]]; then
	yarn install --frozen-lockfile
    node_modules/@angular/cli/bin/ng build
fi
cd - > /dev/null

# deploy frontend
cd code
serverless client deploy --no-confirm
CLIENT_BUCKET=$(jq ".service.custom.client.bucketName" ./.serverless/serverless-state.json | xargs)
cd - > /dev/null

#open browser
if [[ $1 != "--no-browser" ]]; then
    xdg-open "http://${CLIENT_BUCKET}.s3-website.eu-central-1.amazonaws.com/" 2>/dev/null > /dev/null
    sleep 2
    echo -e "\n\n\n\n"
fi
