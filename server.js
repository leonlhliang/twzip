#!/usr/bin/env node
var express = require("express");
var morgan  = require("morgan");

var mode = process.env.mode || "test";
var port = process.env.port || 3000;


var server = express();

if (mode !== "test") { server.use(morgan("combined")); }

server.use(function (req, res, next) {
    var lang = req.query.lang || "zh-tw";
    if (["en-us", "zh-tw"].indexOf(lang) === -1) { return res.status(404).json({
        message: "lang parameter must be one of: zh-tw, en-us"
    });}
    req.lang = lang;
    return next();
});

server.route("/v1/zipcode").get(function (req, res) {
    if (!req.query.address) { return res.status(400).json({
        message: "missing required field address",
        example: "?address=somewhere"
    });}
    return res.status(200).json({zipcode: "00000"});
});

server.route("/v1/districts").get(function (req, res) {
    return res.json({language: req.lang, districts: []});
});

server.route("/v1/cities").get(function (req, res) {
    return res.json({language: req.lang, cities: []});
});

server.route("/v1/roads").get(function (req, res) {
    return res.json({language: req.lang, roads: []});
});

server.route("/status").get(function (req, res) {
    return res.status(200).json({language: req.lang, version: "0.1.0"});
});

server.use(function (err, req, res, next) {
    var detail = [req.path, err.stack].join("\n");
    if (mode === "test") { return res.status(500).send(detail); }
    res.status(500).send("server error");
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
