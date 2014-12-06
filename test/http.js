var supertest = require("supertest");
var path      = require("path");

var filepath = path.join(process.cwd(), "server");
var request  = supertest(require(filepath));


module.exports = function () {

    this.Given(/^an express instance loaded as server$/, function (next) {
        return next();
    });

    this.Given(/^request to (.*) will respond with (.*)$/, function (url, code, next) {
        return request.get(url).expect(200, next);
    });

};
