#!/usr/bin/env bash

cd code
{
    prompt_mode=true

    # for testing purpose add true as parameter
    if [ $# -eq 1 ]; then
        prompt_mode=false
    fi

    function_array=$(serverless info | grep GET | sed 's/  GET - //g ')
    if [[ -z ${function_array} ]]; then
        echo "[ERROR] Please deploy first!"
        exit
    fi

    python3 load_generator/lambda_call_generator.py $prompt_mode $function_array
}||{
    cd - > /dev/null
}
