#!/usr/bin/env node
var server = require("./lib")(process.env.mode || "local");
var port   = process.env.port || 3000;

console.log("server running at http://localhost:%d ...", port);
server.listen(port);
