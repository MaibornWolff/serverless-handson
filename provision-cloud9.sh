#!/usr/bin/env bash
set -e

npm install -g yarn serverless@3.23.0

cd task2/src
sudo pip3 install -r requirements.txt
npm install
