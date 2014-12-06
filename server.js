var express = require("express");
var morgan  = require("morgan");


var server = express();

server.use(morgan("combined"));


server.route("/v1/cities").get(function (req, res) {
    res.send(req.query);
});

server.route("/v1/zip").get(function (req, res) {
    res.send(req.query);
});


server.listen(3000);
