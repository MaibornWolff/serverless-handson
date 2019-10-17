# Serverless - Hands On

Enclosed you will find the code for the examples of a guided Serverless Hands On.

#### Notes
- The sources were created especially for this event and are only available to the participants.
- The examples were tailored to specific target groups - i.e. they were didactically adapted to convey the concepts in the best possible way.
- The code and documentation do not reflect MaibornWolff's qualitative requirements for productive use.
- If you have any questions, please contact MaibornWolff directly e.g. michael.abey@maibornwolff.de


### Prerequisite for Cloud9 Web IDE

If you use Cloud9, please start the provisioning script by open a Terminal in your Cloud9 Web IDE and enter:
```
cd serverless-handson
./provision.sh
```

#### Operating system
It has been tested for the following operating systems:
- Linux
- OSX

#### Cloud Account
- Create AWS account + store credentials in operating system (currently only as default)
 
 
    vi ~/.aws/credentials
    [default]
    aws_access_key_id = AKIA...
    aws_secret_access_key = r4VAd....


#### Set environment variables

    export GROUP_ID=1
    export ELASTIC_IP=<ip_to_running_elastic>
    
#### Central monitoring
We've set up a central elastic stack for this Hands On. We cannot add this to the sources.
Examples that depend on it would have to be skipped or an Elasticsearch and Kibana would have to be provided.
This concerns task 3+4 


#### Testing
For a complete automated testing of all examples, a smoketest was written that goes through the rough functionalities once.
It also queries all technically installed prerequisites, which may have to be installed manually.


    cd internals
    ./smoke-test.sh
    
Test individual tasks by number e.g.

    ./smoke-test.sh 1
    
    
#### Delete
If a test goes wrong or a task has to be cleaned up again

    cd internals
    ./destroy-task.sh
    
    
## examples - task
Please find in the enclosed presentation and in the taskN/README.md


## Example - Execute
The examples are all structured in the same way:

    
    /taskN
    	/code
    		/serverless_functions  - Serverless Functions
    		/hint                  - hints to solve the task
    	serverless.yml                 - Serverless Framework Configuration
    	./deploy.sh                    - deploy script
    	README.md                      - Documentation

Please follow the instructions in the tasks in the folders:
/task1 ... N

There you will find all the information you need to execute the examples.