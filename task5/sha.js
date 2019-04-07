const crypto = require("crypto");
var shell = require('./code/node_modules/shelljs');

module.exports = (serverless) => {
    return shell.exec("aws iam list-users --output json| jq '.Users[0].UserName'| tr -d \\\"",{silent:true}).stdout
}
