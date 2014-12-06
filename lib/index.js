var express = require("express");
var morgan  = require("morgan");


var app = express();


module.exports = function (mode) {
    if (mode) { app.use(morgan("combined")); }

    app.route("/v1/cities").get(function (req, res) {
        res.send(req.query);
    });

    app.route("/v1/zip").get(function (req, res) {
        res.send(req.query);
    });

    return app;
};
