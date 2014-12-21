var supertest = require("supertest-as-promised");
var path      = require("path");
var chai      = require("chai");

var server = supertest(require(path.join(process.cwd(), "server")));


module.exports = function () {
    var expect = chai.expect;

    this.Given(/^an express server loaded as target$/, function (next) {
        return next();
    });

    this.When(/^send a (.*) request to (.*)$/, function (method, url, next) {
        method = method.toLowerCase();
        this.expected = {url: url, method: method};
        /* istanbul ignore else */
        if (method === "get") { this.expected.queries = []; }
        return next();
    });

    this.When(/^append URL with "(.*)" query$/, function (query, next) {
        this.expected.queries.push(query);
        return next();
    });

    this.Then(/^receive a JSON response of (\d+)$/, function (status, next) {
        this.expected.status = parseInt(status);
        this.expected.type = "application/json";
        return next();
    });

    this.Then(/^body have "(.*)" with "(.*)"$/, function (key, value, next) {
        var expected = this.expected, queries = [];
        return server[expected.method](expected.url).
        query(expected.queries.join("&")).expect(expected.status).
        then(function (res) {
            expect(res.type).to.equal(expected.type);
            expect(res.body).to.have.property(key).and.to.equal(value);
            return next();
        }).catch(function (err) {
            return next.fail(err);
        });
    });

};
