var runexec = require("bluebird").promisify(require("child_process").exec);
var fsrdir  = require("bluebird").promisify(require("fs").readdir);
var fsopen  = require("bluebird").promisify(require("fs").open);
var expect  = require("chai").expect;
var path    = require("path");


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

    this.Then(/^have a valid JSON at "([^"]*)"$/, function (file, next) {
        var filepath = path.join(process.cwd(), file);
        expect(require(filepath)).to.be.an("object");
        return next();
    });

    this.Then(/^file "([^"]*)" contains sample:$/, function (file, table, next) {
        var filepath = path.join(process.cwd(), file), name = null;

        expect(require(filepath)).to.be.an("object");
        name = require(filepath);

        table.raw().forEach(function (row) {
            expect(name).to.have.property(row[0]);
            expect(name[row[0]]["name"][0]).to.equal(row[1]);
            expect(name[row[0]]["name"][1]).to.equal(row[2]);
        });

        return next();
    });

    this.Then(/^folder "([^"]*)" holds folders:$/, function (dir, table, next) {
        return fsrdir(path.join(process.cwd(), dir)).then(function (dirs) {
            table.raw().forEach(function (row) {
                row.forEach(function (col) {
                    expect(dirs).to.include(col);
                });
            });
            return next();
        }).catch(function (err) {
            return next.fail(err);
        });
    });

};
