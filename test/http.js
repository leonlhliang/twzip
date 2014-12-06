var app = require(require("path").join(process.cwd(), "lib"));
var req = require("supertest")(app());


module.exports = function () {

    this.Given(/^request to (.*) will respond with (.*)$/, function (url, code, next) {
        return req.get(url).expect(200, next);
    });

};
