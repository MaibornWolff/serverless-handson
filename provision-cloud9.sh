#!/bin/bash
npm install -g yarn serverless@2.5
# Deactivate until new setup with newer python version is ready
# sudo pip install requests requests-toolbelt

cd task2/src && npm init -y && npm install --save serverless-python-requirements
