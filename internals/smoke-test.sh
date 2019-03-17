#!/usr/bin/env bash

echo "TEST - TASK1 - local monolith"
cd ../task1/code/monolith
python monolith_app.py
cd -

echo "TEST - TASK1 - serverless functions"
cd ../task1/internal
./deploy.sh
#TODO: do we need to curl the link?
serverless invoke -f hello -l
serverless logs -f hello -t
cd -
./destroy-task1.sh

echo "TEST - TASK1 - cleanup"
#TODO: remove all created files

#....