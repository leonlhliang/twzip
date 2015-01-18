#!/usr/bin/env node
var express = require("express");
var morgan  = require("morgan");

var version = require("./package.json").version;
var postal  = require("./postal");


var mode = process.env.MODE || "test";
var port = process.env.PORT || "3000";


var server = express().disable("x-powered-by");

/* istanbul ignore if */
if (mode !== "test") { server.use(morgan("combined")); }

server.use(function (req, res, next) {
    req.query.lang = req.query.lang || "zh-TW";
    if (["en-US", "zh-TW"].indexOf(req.query.lang) !== -1) { return next(); }
    return res.status(404).json({
        message: "supported languages: zh-TW, en-US"
    });
});

server.route("/v1/districts").get(postal.district);
server.route("/v1/zipcode").get(postal.zipcode);
server.route("/v1/streets").get(postal.street);
server.route("/v1/cities").get(postal.city);

server.route("/status").get(function (req, res) {
    return res.status(200).json({
        language: req.query.lang,
        version: version
    });
});

server.route("/*").all(function (req, res) {
    return res.status(404).json({
        message: "notfound"
    });
});

/* istanbul ignore next */
server.use(function (err, req, res, next) {
    var detail = [req.path, err.stack].join("\n");
    res.status(500).type("text/plain");
    if (mode === "test") { return res.send(detail); }
    res.send("server error");
    return next;
});


/* istanbul ignore else */
if (mode === "test") {
    module.exports = server;
} else if (mode === "local") {
    console.log("server running at http://localhost:%d ...", port);
    server.listen(port);
} else {
    server.listen(port);
}
