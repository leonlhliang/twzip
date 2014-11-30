var runexec = require("bluebird").promisify(require("child_process").exec);
var expect  = require("chai").expect;
var path    = require("path");


module.exports = function () {

    this.Given(/^the official data as "([^"]*)"$/, function (filename, next) {
        expect(filename).to.equal("ORIGIN.txt");
        return next();
    });

    this.When(/^execute the command "([^"]*)"$/, function (cmd, next) {
        return runexec(cmd).spread(function () {
            return next();
        }).catch(function (err) {
            return next.fail(err);
        });
    });

    this.Then(/^have a valid JSON named "([^"]*)"$/, function (filename, next) {
        var filepath = path.join(process.cwd(), filename);
        expect(require(filepath)).to.be.an("object");
        return next();
    });

};
