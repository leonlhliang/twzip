var supertest = require("supertest-as-promised");
var path      = require("path");
var chai      = require("chai");

var filepath = path.join(process.cwd(), "server");
var request  = supertest(require(filepath));


module.exports = function () {

    this.Given(/^an express instance loaded as server$/, function (next) {
        try { chai.expect(request).is.not.undefined; }
        catch (err) { return next.fail(err); }
        return next();
    });

    this.When(/^send http (.*) to (.*)$/, function (method, endpoint, next) {
        var methods = ["get", "post", "put", "delete"];
        method = method.toLowerCase();
        try { chai.expect(methods).to.include(method); }
        catch (err) { return next(err); }
        this.req = { endpoint: endpoint, method: method, query: {} };
        return next();
    });

    this.Given(/^specify "([^"]*)" in query string$/, function (query, next) {
        if (!this.req) { return next.fail(new Error("no request")); }
        query = query.split("=");
        try { chai.expect(query.length).to.equal(2); }
        catch (err) { return next.fail(err); }
        this.req.query[query[0]] = query[1];
        return next();
    });

    this.Then(/^receive a (.*) response$/, function (type, next) {
        if (!this.req) { return next.fail(new Error("no request")); }
        try { chai.expect(type).to.equal("JSON"); }
        catch (err) { return next.fail(err); }
        this.req.type = "application/json";
        return next();
    });

    this.Then(/^status code is (\d+)$/, function (status, next) {
        if (!this.req) { return next.fail(new Error("no request")); }
        try { status = parseInt(status); }
        catch (err) { return next.fail(err); }
        this.req.status = status;
        return next();
    });

    this.Then(/^body contains fields:$/, function (table, next) {
        var given = this.req;
        if (!given) { return next.fail(new Error("no request")); }
        if (given.method === "get" && given.query) {
            given.endpoint += "?";
            for (var field in given.query) {
                given.endpoint += [field, given.query[field]].join("=");
            }
        }
        return request[given.method](given.endpoint).
        expect(given.status).then(function (res) {
            chai.expect(res.type).to.equal(given.type);
            table.hashes().forEach(function (field) {
                chai.expect(res.body).to.have.
                property(field.name).and.to.
                equal(field.value);
            });
            return next();
        }).catch(function (err) {
            return next.fail(err);
        });
    });

};
