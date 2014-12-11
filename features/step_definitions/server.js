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
        var methods = ["get", "post", "put", "delete"];
        method = method.toLowerCase();
        try { expect(methods).to.include(method); }
        catch (err) { return next(err); }
        this.expected = {endpoint: endpoint, method: method};
        if (method === "get") { this.expected.queries = []; }
        return next();
    });

    this.When(/^append URL with (.*) string$/, function (query, next) {
        try {
            expect(this.expected).is.an("object");
            expect(this.expected.method).to.equal("get");
            expect(query.split("=").length).to.equal(2);
        } catch (err) { return next.fail(err); }
        this.expected.queries.push(query);
        return next();
    });

    this.Then(/^receive a JSON response of (\d+)$/, function (status, next) {
        try { status = parseInt(status); }
        catch (err) { return next.fail(err); }
        this.expected.type = "application/json";
        this.expected.status = status;
        return next();
    });

    this.Then(/^body contains (.*) with (.*)$/, function (field, value, next) {
        var expected = this.expected, queries = [];
        try { expect(expected).to.be.an("object"); }
        catch (err) { return next.fail(err); }
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
