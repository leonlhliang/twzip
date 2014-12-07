#!/usr/bin/env node
var promise = require("bluebird");
var path    = require("path");
var fs      = require("fs");

var recursive = promise.promisify(require("recursive-readdir"));
var fswrite   = promise.promisify(fs.writeFile);

var workdir = path.join(process.cwd(), "lib");


recursive(workdir, ["name.json", "code.json"]).then(function (filepaths) {
    return promise.all(filepaths.map(function (filepath) {
        return {path: filepath, src: require(filepath)};
    }).map(function (area) {
        for (var road in area.src) { area.src[road] = "QQ"; }
        area.src = JSON.parse(area.src).stringify();
        return fswrite(area.path.replace(".json", ".js"), area.src);
    }));
}).then(function () {
    console.log("AA");
}).catch(function (err) {
    console.log(err);
});

