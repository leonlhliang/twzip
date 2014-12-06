var path = require("path");
var req  = require("supertest");


module.exports = function () {

    this.Given(/^an express instance loaded as server$/, function (next) {
        var filepath = path.join(process.cwd(), "server");
        try { req = req(require(filepath)); } catch (e) { return next.fail(e); }
        return next();
    });

    this.Given(/^request to (.*) will respond with (.*)$/, function (url, code, next) {
        return req.get(url).expect(200, next);
    });

};
