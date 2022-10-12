# Serverless - Hands-on

Enclosed you will find the code for the examples of a guided Serverless Hands-on.

## Notes

- The sources were created especially for this event and are only available to the participants.
- The examples were tailored to specific target groups - i.e. they were didactically adapted to convey the concepts in the best possible way.
- The code and documentation do not reflect MaibornWolff's qualitative requirements for productive use.
- If you have any questions, please contact MaibornWolff directly

## Prerequisite for Cloud9 Web IDE

If you use Cloud9, please start the provisioning script by open a Terminal in your Cloud9 Web IDE and enter:

```bash
cd serverless-handson
./provision-cloud9.sh
```

## Operating system

It has been tested for the following operating systems:

- Linux

## Delete

If a test goes wrong or a task has to be cleaned up, please run:

```bash
cd internals
./destroy-task.sh
```

## Structure

The tasks are all structured in the same way:

```text
    /taskN
        /code
            /serverless_functions  - Serverless Functions
            /hint                  - hints to solve the task
        serverless.yml             - Serverless Framework Configuration
        ./deploy.sh                - deploy script
        README.md                  - Documentation
```
