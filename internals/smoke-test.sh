#!/bin/bash
###### LIBRARY-START
function assert {
    local subject="${1}"
    local contains="${2}"
    response=`${3} 2>&1`

    if [[ "${4}" == "show" ]]; then
        echo ${response}
    fi

    if grep -q "${contains}" <<< "${response}"; then
        echo -e "\e[32mOK\e[0m\t ${subject} \t ${contains}"
    else
        echo -e "\e[31mFAILED!\e[0m \t ${subject} \t  Not found ${contains}"
        echo ${response}; exit 1
    fi
}

function --- {
    local printLine="[${1}]:${2}"
    local count=$(( $(tput cols) - `echo ${printLine}|wc -c` ))
    printf "${printLine}%*s\n" "${count}" '' | tr ' ' -
}
###### LIBRARY-END


--- Setup "preconditions"
assert python "Python 3" "python3 --version"
assert dialog "/dialog" "whereis dialog"
assert aws-account "AWS_PROFILE" "printenv"

--- Task1 "monolith"
assert monolith "localhost:9000" "../task1/code/monolith/monolith_server.py --test-mode"

--- Task1 "serverless (~2min)"
cd ../task1/
assert sls-setup "Stack update finished..." "./deploy.sh"
cd - > /dev/null

cd ../task1/code/
assert sls-func "Hello from" "serverless invoke -f hello1 -l"

# get url from 2nd f(x)
URL=`sls info | grep dev/hello2 | xargs |cut -d " " -f3`
assert sls-curl-call  "Go Serverless" "curl $URL"
cd - > /dev/null

assert sls-destroy "Stack removal finished..." "./destroy-task.sh 1"


--- Task1 "cleanup"
assert cleanup "cleanup finished" "./cleanup-task.sh 1"