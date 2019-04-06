#!/bin/bash -e

if [[ $# -eq 0 ]]; then
    RUN_TASKS="1 2 3 4 5"
    echo "Delete all"
else
    RUN_TASKS=$1
fi

for i in ${RUN_TASKS}; do
    case "${i}" in
        1|all)
            echo "... Task1"
            cd ../task1/code
            serverless remove 2>&1 >/dev/null || true
            cd - > /dev/null
            rm -rf ../task1/code/.serverless
        ;;
        2|all)
            echo "... Task2"
        ;;
        3|all)
            echo "... Task3"
        ;;
        4|all)
            echo "... Task4"
        ;;
        5|all)
            echo "... Task5"
            cd ../task5/code
            yarn
            serverless client remove --no-confirm
            serverless remove 2>&1 >/dev/null || true
            cd - > /dev/null
            rm -rf ../task5/code/.serverless
            rm -rf ../task5/code/node_modules
            rm -rf ../task5/frontend/node_modules
        ;;
    esac
    echo -e "... cleaned \e[92m✓\e[39m"
done