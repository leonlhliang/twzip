var express = require("express");


var server = express();

server.use(require("morgan")("combined"));


server.route("/v1/cities").get(function (req, res) {
    res.send(req.query);
});

server.route("/v1/zip").get(function (req, res) {
    res.send(req.query);
});


server.listen(3000);
