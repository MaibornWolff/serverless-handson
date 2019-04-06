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
        printf "    \e[32mOK\e[0m    %-17s %s\n" "${subject}" "${contains}"
    else
        printf "  \e[31mFAILED\e[0m  %-17s %s\n" "${subject}" "${contains}"
        echo ${response}; exit 1
    fi
}

function --- {
    local printLine="[${1}]:${2}"
    local count=$(( $(tput cols) - `echo ${printLine}|wc -c` ))
    printf "\n${printLine}%*s\n" "${count}" '' | tr ' ' _
}
###### LIBRARY-END

--- Setup "preconditions"
assert python "Python 3" "python3 --version"
assert node-yarn "/yarn" "which yarn"
assert node-npm "/npm" "which npm"
assert sls "/sls" "which sls"
assert serverless "/serverless" "which serverless"
assert jq "/jq" "which jq"
assert aws-account "AWS_PROFILE" "printenv"
if [[ "$OSTYPE" == "darwin"* ]]; then
    assert open "/open" "which open"
else
    assert xdg-open "/xdg-open" "which xdg-open"
    assert firefox "Mozilla Firefox" "firefox -v"
fi




#introduce try-catch
{

    --- Task1 "monolith"
    assert monolith "localhost:9000" "../task1/code/monolith/monolith_server.py --test-mode"

    --- Task1 "serverless (~2min)"
    cd ../task1/
    assert sls-setup "Stack update finished..." "./deploy.sh"
    cd - > /dev/null

    cd ../task1/code/
    assert sls-func "Hello from" "serverless invoke -f brightness -l"

    # get url from 2nd f(x)
    URL=`sls info | grep production/brightness | xargs |cut -d " " -f3`
    assert sls-url-given "http" "$URL"
    assert sls-curl-call  "Go Serverless" "curl -X GET $URL"
    assert sls-destroy "Stack removal finished..." "sls remove"
    cd - > /dev/null

    assert cleanup "cleaned" "./destroy-task.sh 1"



    --- Task3 "serverless (~2min)"
    cd ../task3/
    assert sls-setup "Stack update finished..." "./deploy.sh"
    cd - > /dev/null

    cd ../task3/code/
    assert sls-func "Sent temperature to monitoring" "serverless invoke -f temperature -l"

    URL=`sls info | grep production/temperature | xargs |cut -d " " -f3`
    assert sls-url-given "http" "$URL"
    assert sls-curl-call  "Temperature retrieved successfully" "curl -X GET $URL"
    assert sls-destroy "Stack removal finished..." "sls remove"
    cd - > /dev/null

    assert cleanup "cleaned" "./destroy-task.sh 3"



    --- Task5 "serverless (~3min)"
    cd ../task5
    assert sls-setup "Stack update finished..." "./deploy.sh --no-browser"
    cd - > /dev/null

    cd ../task5/code/
    assert sls-voices "Polly not found" "serverless invoke -f voices -l"

    assert sls-synth '\\"speech\\":' "serverless invoke -f speechSynthesize -l -p ../../internals/events/polly-demo.json"

    URL=`sls info | grep production/voices | xargs |cut -d " " -f3`
    assert sls-url-given "http" "$URL"
    assert sls-curl-call  "Polly not found" "curl -X GET $URL"
    assert sls-destroy "Stack removal finished..." "sls remove"
    cd - > /dev/null

    assert cleanup "cleaned" "./destroy-task.sh 5"

}||{
    echo "failed: Cleanup everything"
    ./destroy-task.sh
}

