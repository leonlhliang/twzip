var runexec = require("bluebird").promisify(require("child_process").exec);
var expect  = require("chai").expect;
var path    = require("path");
var fsopen  = require("bluebird").promisify(require("fs").open);


module.exports = function () {

    this.Given(/^official documents are in place:$/, function (table, next) {
        expect(table.raw().length).to.equal(2);
        expect(table.raw().filter(function (row) {
            var filepath = path.join(process.cwd(), row[0]);
            return fsopen(filepath, "r").spread(function () {
                return true;
            }).catch(function () {
                return false;
            });
        }).length).to.equal(table.raw().length);
        return next();
    });

    this.When(/^execute the command "([^"]*)"$/, function (cmd, next) {
        return runexec(cmd).spread(function () {
            return next();
        }).catch(function (err) {
            return next.fail(err);
        });
    });

    this.Then(/^have a valid JSON at "([^"]*)"$/, function (filename, next) {
        var filepath = path.join(process.cwd(), filename);
        expect(require(filepath)).to.be.an("object");
        return next();
    });

};
