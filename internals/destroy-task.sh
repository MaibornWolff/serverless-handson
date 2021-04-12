#!/bin/bash -e

RUN_TASKS=`test $# -eq 0 && echo "0 1 2" || echo $1`

for i in ${RUN_TASKS}; do
    case "${i}" in
        0)
            echo "...Task0"
            cd ../task0/src
            serverless remove 2>&1 >/dev/null || true
            cd - > /dev/null
            rm -rf ../task0/src/.serverless
        ;;
        1)
            echo "...Task1"
            cd ../task1/src
            serverless remove 2>&1 >/dev/null || true
            cd - > /dev/null
            rm -rf ../task1/src/.serverless
        ;;
        2)
            echo "...Task2"
            cd ../task2/src
            serverless remove 2>&1 >/dev/null || true
            cd - > /dev/null
            rm -rf ../task2/src/.serverless
        ;;
    esac
    echo -e "...cleaned \e[92m✓\e[39m"
done
