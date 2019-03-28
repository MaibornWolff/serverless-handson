#!/usr/bin/env bash

set -e
# deploy backend
cd code
yarn
serverless deploy -v
BASE_URL=`sls info -v | grep ServiceEndpoint: | xargs |cut -d " " -f2`
cd - > /dev/null

sed -i -E "s?lambdaApiEndpoint:.+?lambdaApiEndpoint: '${BASE_URL}'?g" ./frontend/src/environments/environment.ts
sed -i -E "s?lambdaApiEndpoint:.+?lambdaApiEndpoint: '${BASE_URL}'?g" ./frontend/src/environments/environment.prod.ts

# build frontend
cd frontend
yarn
ng build --prod
cd - > /dev/null

# deploy frontend
cd code
serverless client deploy --no-confirm
CLIENT_BUCKET=$(jq ".service.custom.client.bucketName" ./.serverless/serverless-state.json | xargs)
cd - > /dev/null

#open browser
xdg-open "http://${CLIENT_BUCKET}.s3-website.eu-central-1.amazonaws.com/" 2>&1 > /dev/null