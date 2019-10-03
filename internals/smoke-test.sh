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

RUN_TASKS=`test $# -eq 0 && echo "1 2 3 4 5" || echo $1`


--- Setup "preconditions"
assert python "Python 3" "python3 --version"
assert node-yarn "/yarn" "which yarn"
assert node-npm "/npm" "which npm"
assert sls "/sls" "which sls"
assert serverless "/serverless" "which serverless"
assert jq "/jq" "which jq"
assert GROUP_ID "\"UserName\": \"${GROUP_ID}\"" "aws iam list-users --output json"
assert kibana-exists "Kibana" "curl -X GET http://18.184.206.122:5601/app/kibana"




#introduce try-catch
{
    for i in ${RUN_TASKS}; do
        case "${i}" in
            1)
                --- Task1 "monolith"
                assert monolith "localhost:9000" "../task1/code/monolith/monolith_server.py --test-mode"

                --- Task1 "serverless (~2min)"
                cd ../task1/
                assert sls-setup "Stack update finished..." "./deploy.sh"
                cd - > /dev/null

                cd ../task1/code/
                assert sls-func "unexpected EOF while parsing" "serverless invoke -f brightness -l"

                # get url from 2nd f(x)
                URL=`sls info | grep production/brightness | xargs |cut -d " " -f3`
                assert sls-url-given "http" "$URL"
                assert sls-curl-call  "Internal server error" "curl -X GET $URL" "show"
                assert sls-destroy "Stack removal finished..." "sls remove"
                cd - > /dev/null

                assert cleanup "cleaned" "./destroy-task.sh 1"
            ;;
            2)
                --- Task2 "serverless (~2min)"
                cd ../task2/
                assert sls-setup "Stack update finished..." "./deploy.sh"
                cd - > /dev/null

                cd ../task2/code/
                assert sls-func "Your serverless function executed successfully!" "serverless invoke -f wind -l"

                URL=`sls info | grep production/brightness | xargs |cut -d " " -f3`
                assert sls-url-given "http" "$URL"
                assert sls-curl-call  "Your serverless function executed successfully!" "curl -X GET $URL"
                assert sls-destroy "Stack removal finished..." "sls remove"
                cd - > /dev/null

                assert cleanup "cleaned" "./destroy-task.sh 2"
            ;;
            3)
                --- Task3 "serverless (~2min)"
                # precondition
                export GROUP_ID=99

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
            ;;
            4)
                --- Task4 "serverless (~2min)"
                # precondition
                export GROUP_ID=88

                cd ../task4/
                assert sls-setup "Stack update finished..." "./deploy.sh"
                cd - > /dev/null

                cd ../task4/code/
                assert sls-func "There are high temperatures" "serverless invoke -f temperature -l"

                URL=`sls info | grep production/temperature | xargs |cut -d " " -f3`
                assert sls-url-given "http" "$URL"
                assert sls-curl-call  "Temperature retrieved successfully" "curl -X GET $URL"
                cd - > /dev/null

                cd ../task4/
                assert sls-kibana-call "Test was successfully" "./dark-clouds.sh false"
                cd - > /dev/null

                cd ../task4/code/
                assert sls-destroy "Stack removal finished..." "sls remove"
                cd - > /dev/null

                assert cleanup "cleaned" "./destroy-task.sh 4"
            ;;
            5)
                --- Task5 "serverless (~3min)"
                cd ../task5
                assert sls-setup "Success! Your site should be available at" "./deploy.sh --no-browser"
                cd - > /dev/null

                cd ../task5/code/
                assert sls-voices "Gender" "serverless invoke -f voices -l"

                assert sls-synth '\\"speech\\":' "serverless invoke -f speechSynthesize -l -p ../../internals/events/polly-demo.json"

                URL=`sls info | grep production/voices | xargs |cut -d " " -f3`
                assert sls-url-given "http" "$URL"
                assert sls-curl-call  "\"Gender\": \"Female\"" "curl -X GET $URL"
                assert sls-destroy "Stack removal finished..." "sls remove"
                cd - > /dev/null

                assert cleanup "cleaned" "./destroy-task.sh 5"
            ;;
        esac
    done

}||{
    echo "failed: Cleanup everything"
    ./destroy-task.sh
}

