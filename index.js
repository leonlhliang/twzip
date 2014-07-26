var rule = require("./lib");


var parse = function (numbers) {
    "use strict";
    return {
        idx: 0,
        aly: 0,
        flr: 0,
        ext: 0,
        ln: 0,
        no: 0
    };
};


module.exports = function (city, district, street, numbers) {
    "use strict";
    return rule[city][district][street](parse(numbers));
};
