const crypto = require("crypto");

var arped = require('./code/node_modules/get-mac-address');

function shortSha256(data) {
    return crypto.createHash("sha256").update(data).digest("hex");
}

module.exports = (serverless) => {
    let localMacAddress = arped[Object.keys(arped).slice(-1).pop()]
    let hash = shortSha256( localMacAddress ).slice(-6);
    serverless.cli.consoleLog('Using random string suffix '+hash);
    return hash;
}
