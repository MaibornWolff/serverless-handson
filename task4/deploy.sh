#!/bin/bash -e

cd code
sls plugin install -n serverless-python-requirements
serverless deploy -v
cd -