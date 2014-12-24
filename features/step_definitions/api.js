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
        this.expected.queries = [];
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

    this.Then(/^body's "([^"]*)" equals "([^"]*)"$/, function (key, val, next) {
        var given = this.expected;
        return server[given.method](given.url).
        query(given.queries.join("&")).
        expect(given.status).
        then(function (res) {
            expect(res.type).to.equal(given.type);
            expect(res.body).to.have.property(key).and.to.equal(val);
            return next();
        });
    });

};
