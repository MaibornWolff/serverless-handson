#!/usr/bin/env bash

echo "REMOVE - TASK4 - serverless functions"
cd ../task4/code
serverless remove -v
rm -rf .serverless
cd -