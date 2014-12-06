#!/usr/bin/env node
var express = require("express");
var morgan  = require("morgan");

var mode = process.env.MODE || "test";
var port = process.env.PORT || 3000;


var server = express();

if (mode !== "test") { server.use(morgan("combined")); }


server.route("/v1/zipcode").get(function (req, res) {
    res.send(req.query);
});

server.route("/v1/cities").get(function (req, res) {
    res.send(req.query);
});

server.route("/status").get(function (req, res) {
    res.status(200).type("text/plain").send("OK");
    return req;
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
