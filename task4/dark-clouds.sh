#!/usr/bin/env bash

cd code
{
    function_array=$(serverless info | grep GET | sed 's/  GET - //g ')
    python3 load_generator/lambda_call_generator.py $function_array
}||{
    cd - > /dev/null
}
