var supertest = require("supertest");
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
        try { this.resp = request[method.toLowerCase()](endpoint); }
        catch (err) { return next.fail(err); }
        return next();
    });

    this.Then(/^receive response of (\d+)$/, function (status, next) {
        if (!this.resp) { return next.fail(new Error("no responses")); }
        try { status = parseInt(status); }
        catch (err) { return next.fail(err); }
        return this.resp.expect(status, next);
    });

};
