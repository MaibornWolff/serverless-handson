#!/bin/bash -e

if [[ $# -eq 0 ]]; then
    echo "pass task number please"
    exit 1
fi

case "${1}" in
    1) rm -rf ../task1/code/.serverless ;;
    2) ;;
    3) ;;
    4) ;;
    5) rm -rf ../task5/code/.serverless && rm -rf ../task5/code/node_modules && rm -rf ../task5/frontend/node_modules && rm -rf ../task5/frontend/dist;;
esac

echo "cleanup finished"