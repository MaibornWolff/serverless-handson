# Serverless - Hands-On

Enclosed you will find the code for the examples of a guided Serverless Hands-On.

#### Notes
- The sources were created especially for this event and are only available to the participants.
- The examples were tailored to specific target groups - i.e. they were didactically adapted to convey the concepts in the best possible way.
- The code and documentation do not reflect MaibornWolff's qualitative requirements for productive use.
- If you have any questions, please contact MaibornWolff directly.

### Prerequisite for Cloud9 Web IDE
If you use Cloud9, please start the provisioning script by open a terminal in your Cloud9 Web IDE and enter:
```
cd serverless-handson
./provision.sh
```

#### Operating system
It has been tested for the following operating systems:
- Linux
- OS X

#### Delete
If a test goes wrong or a task has to be cleaned up, please run:
```
cd internals
./destroy-task.sh
```

## Structure
The tasks are all structured in the same way:

```
    /taskN
    	/src
    		/serverless_functions  - Serverless functions
    		/hint                  - Hints to solve the task (if any)
    	serverless.yml                 - Configuration of Serverless Framework
    	README.md                      - Documentation (if any)
```
