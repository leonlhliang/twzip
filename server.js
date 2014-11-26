var express = require("express");
var morgan  = require("morgan");

var server = express();

server.use(morgan("combined"));

server.get("/v1/zip", function (req, res) {
    res.send(req.query);
});

server.listen(3000);
