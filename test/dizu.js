var promise = require("bluebird");
var runexec = promise.promisify(require("child_process").exec);
var chai    = require("chai");
var path    = require("path");
var fs      = promise.promisifyAll(require("fs"));


chai.use(require("chai-as-promised"));


module.exports = function () {

    this.Given(/^required documents are in place:$/, function (table, next) {
        return promise.all(table.raw().map(function (row) {
            return row.map(function (col) {
                return fs.openAsync(path.join(process.cwd(), col), "r");
            });
        })).then(function () {
            return next();
        }).catch(function (err) {
            return next.fail(err);
        });
    });

    this.When(/^execute the command "([^"]*)"$/, function (cmd, next) {
        return runexec(cmd).then(function () {
            return next();
        }).catch(function (err) {
            return next.fail(err);
        });
    });

    this.Then(/^have a valid JSON at "([^"]*)"$/, function (file, next) {
        var filepath = path.join(process.cwd(), file);
        return fs.readFileAsync(filepath).then(function (content) {
            JSON.parse(content);
            return next();
        }).catch(function (err) {
            return next.fail(err);
        });
    });

    this.Then(/^file "([^"]*)" holds sample:$/, function (file, table, next) {
        var filepath = path.join(process.cwd(), file);

        return fs.readFileAsync(filepath).then(function (content) {
            var name = JSON.parse(content);
            table.raw().forEach(function (row) {
                chai.expect(name).to.have.property(row[0]).
                and.to.have.property("name").
                and.to.be.an("array").
                and.to.deep.equal([row[1], row[2]]);
            });
            return next();
        }).catch(function (err) {
            return next.fail(err);
        });
    });

    this.Then(/^folder "([^"]*)" holds folders:$/, function (dir, table, next) {
        var target = path.join(process.cwd(), dir);
        return fs.readdirAsync(target).then(function (dirs) {
            table.raw().forEach(function (row) {
                row.forEach(function (col) {
                    chai.expect(dirs).to.include(col);
                });
            });
            return next();
        }).catch(function (err) {
            return next.fail(err);
        });
    });

    this.Then(/^each area in "([^"]*)" be one "([^"]*)" file$/, function (file, ext, next) {
        var filepath = path.join(process.cwd(), file);

        return fs.readFileAsync(filepath).then(function (content) {
            var map = JSON.parse(content), areas = [];
            for (var city in map) {for (var area in map[city].area) {
                var target = path.join("lib", city, [area, ext].join("."));
                areas.push(fs.openAsync(target, "r"));
            }}
            return promise.all(areas);
        }).then(function () {
            return next();
        }).catch(function (err) {
            return next.fail(err);
        });
    });

};
