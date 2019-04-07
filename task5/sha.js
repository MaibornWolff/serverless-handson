const crypto = require("crypto");
var shell = require('./code/node_modules/shelljs');

module.exports = (serverless) => {
    var username=shell.exec("aws iam list-users --output json| jq '.Users[0].UserName'|tr -d \\\"",{silent:true})
    .stdout.trim();

    if(username==""){
        console.log("No AWS Profile set")
        process.exit(1)
    }
    return username
}
