#!/bin/bash -e

if [[ $# -eq 0 ]]; then
    echo "pass task number please"
    exit 1
fi

case "${1}" in
    1) cd ../task1/code && serverless remove && cd - ;;
    2) ;;
    3) ;;
    4) ;;
    5) cd ../task5/code && serverless client remove --no-confirm && serverless remove && cd - ;;
esac