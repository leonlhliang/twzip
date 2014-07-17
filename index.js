var rule = require("./lib/rule");


var parse = function (numbers) {
    "use strict";
    return {
        number: 0,
        alley: 0,
        floor: 0,
        index: 0,
        lane: 0,
        dash: 0
    };
};


module.exports = function (city, district, street, numbers) {
    "use strict";
    return rule[city][district][street](parse(numbers));
};
