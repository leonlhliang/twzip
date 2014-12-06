var server = require(require("path").join(process.cwd(), "app"));
var req    = require("supertest")(server());


module.exports = function () {

    this.Given(/^request to (.*) will respond with (.*)$/, function (url, code, next) {
        return req.get(url).expect(200, next);
    });

};
