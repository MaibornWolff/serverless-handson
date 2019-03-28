#!/usr/bin/env bash

nohup python3 lambda_call_generator.py 1 10 50 20 40 20 10 15 &

nohup python3 lambda_call_generator.py 2 10 10 30 20 40 10 15 &

nohup python3 lambda_call_generator.py 3 10 10 10 20 10 40 10 &

nohup python3 lambda_call_generator.py 4 10 50 50 50 0 10 10 &

nohup python3 lambda_call_generator.py 5 10 10 20 30 40 50 60 &