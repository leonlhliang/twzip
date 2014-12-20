var supertest = require("supertest-as-promised");
var path      = require("path");
var chai      = require("chai");

var server = supertest(require(path.join(process.cwd(), "server")));


module.exports = function () {
    var expect = chai.expect;

    this.Given(/^an express instance loaded as target server$/, function (next) {
        return next();
    });

    this.When(/^send a (.*) request to (.*)$/, function (method, endpoint, next) {
        method = method.toLowerCase();
        this.expected = {endpoint: endpoint, method: method};
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

    this.Then(/^body contains "(.*)" with "(.*)"$/, function (field, value, next) {
        var expected = this.expected, queries = [];
        return server[expected.method](expected.endpoint).
        query(expected.queries.join("&")).expect(expected.status).
        then(function (res) {
            expect(res.type).to.equal(expected.type);
            expect(res.body).to.have.property(field).and.to.equal(value);
            return next();
        }).catch(function (err) {
            return next.fail(err);
        });
    });

};
