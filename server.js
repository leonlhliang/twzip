#!/usr/bin/env node
var express = require("express");
var morgan  = require("morgan");

var mode = process.env.mode || "test";
var port = process.env.port || "3000";


var server = express();

if (mode !== "test") { server.use(morgan("combined")); }

server.use(function (req, res, next) {
    req.query.lang = req.query.lang || "zh-TW";
    if (["en-US", "zh-TW"].indexOf(req.query.lang) !== -1) { return next(); }
    return res.status(400).json({
        message: "lang must be one of: zh-TW, en-US"
    });
});

server.route("/v1/zipcode").get(function (req, res) {
    if (!req.query.address) { return res.status(400).json({
        message: "parameter 'address' is required",
        example: "?address=somewhere",
        errno: "001"
    });}
    return res.status(200).json({zipcode: "00000"});
});

server.route("/v1/districts").get(function (req, res) {
    return res.json({language: req.query.lang, districts: []});
});

server.route("/v1/streets").get(function (req, res) {
    return res.json({language: req.query.lang, streets: []});
});

server.route("/v1/cities").get(function (req, res) {
    return res.json({language: req.query.lang, cities: []});
});

server.route("/status").get(function (req, res) {
    return res.status(200).json({language: req.query.lang, version: "0.1.0"});
});

server.use(function (err, req, res, next) {
    var detail = [req.path, err.stack].join("\n");
    res.status(500).type("text/plain");
    if (mode === "test") { return res.send(detail); }
    res.send("server error");
    return next;
});


if (mode === "test") {
    module.exports = server;
} else if (mode === "local") {
    console.log("server running at http://localhost:%d ...", port);
    server.listen(port);
} else {
    server.listen(port);
}
