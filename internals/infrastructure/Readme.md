# Installs AWS Cloud 9 via CloudFormation

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Cloud9.html

```
cd aws-cloud9-setup
aws cloudformation create-stack --template-body file://c9.yaml --stack-name something
aws cloudformation delete-stack --stack-name something
```