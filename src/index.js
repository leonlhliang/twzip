exports.district = function (req, res) {
    return res.json({
        districts: [],
        language: req.query.lang
    });
};

exports.zipcode = function (req, res) {
    if (!req.query.address) { return res.status(400).json({
        message: "parameter 'address' is required",
        example: "?address=somewhere",
        code: "001"
    });}
    return res.status(200).json({
        zipcode: "00000"
    });
};

exports.street = function (req, res) {
    return res.json({
        language: req.query.lang,
        streets: []
    });
};

exports.city = function (req, res) {
    return res.json({
        language: req.query.lang,
        cities: []
    });
};
